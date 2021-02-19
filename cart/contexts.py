from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from memberships.views import get_user_membership


def get_logged_user_discount(request):
    """Checks to see if the use is authenticated.
        Looks to get_user_membership function in
        memberships.views for current membership.
        If membership is 'Pro' then add discount to cart."""

    if request.user.is_authenticated:
        current_membership = get_user_membership(request)
        current_membership = str(current_membership.membership)
    else:
        current_membership = False

    if current_membership == "Professional":
        discount = True
        return discount
    else:
        return None


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    discount = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if request.user.is_authenticated:
        user_discount = get_logged_user_discount(request)
        if user_discount:
            discount = total * Decimal(settings.SUB_DISCOUNT_PERCENTAGE / 100)
    else:
        discount = 0

    cart_total = total
    sub_total = cart_total - discount
    if user_discount:
        delivery = 0
    else:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = sub_total + delivery
    discount_percentage = Decimal(settings.SUB_DISCOUNT_PERCENTAGE)

    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'cart_total': cart_total,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount': discount,
        'grand_total': grand_total,
        'discount_percentage': discount_percentage,
    }

    return context
