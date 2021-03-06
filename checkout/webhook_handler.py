from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_invoice_paid_email(self, intent):
        """Sends a finalized invoice email when subscritpion is fully paid."""

        cust_email = intent.customer_email
        period_start = datetime.fromtimestamp(intent.period_start)
        amount_paid = intent.amount_paid / 100
        invoice_pdf = intent.invoice_pdf
        hosted_invoice_url = intent.hosted_invoice_url
        subject = render_to_string(
            'checkout/confirmation_emails/finalized_invoice_subject.txt',
            {'intent': intent,
             'customer_email': cust_email,
             }
        )
        body = render_to_string(
            'checkout/confirmation_emails/finalized_invoice_body.txt',
            {
                'customer_email': cust_email,
                'period_start': period_start,
                'amount_paid': amount_paid,
                'invoice_pdf': invoice_pdf,
                'hosted_invoice_url': hosted_invoice_url, }
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""

        cust_email = order.email

        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order,
             'contact_email': settings.DEFAULT_FROM_EMAIL,
             })
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded webhook from Stripe
        """

        intent = event.data.object
        if intent.description == 'Subscription creation':

            return HttpResponse(
                content=f'Webhook Subscription payments recieved: {event["type"]}',
                status=200
            )

        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        stripe_receipt = intent.charges.data[0].receipt_url
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update the profile information if save_info box was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        """ Creating delay in case web hook is sent before order """
        attempt = 1
        while attempt <= 7:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            order.stripe_receipt = stripe_receipt
            order.save()
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                    stripe_receipt=stripe_receipt,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment intent payment failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook failed received: {event["type"]}',
            status=200)

    def handle_invoice_paid(self, event):
            """Calls the Invoice Paid send email fuction """
            intent = event.data.object
            self._send_invoice_paid_email(intent)
            return HttpResponse(
                content=f'Webhook invoice paid revieved: {event["type"]}',
                status=200
            )

    def handle_subscription_created(self, event):
        """Handles subscription creation events"""
        intent = event.data.object

        return HttpResponse(
            content=f'Webhook subscription_created revieved: {event["type"]}',
            status=200
        )
