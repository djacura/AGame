from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HxqfMDnSE9zSCJz2oGm42Uft9J7C8K9GOWGlLwyvJrdEvBxwFLgYD6Zaori8dreKQ2lygv1DSXYAz2OGGmIRcmj00ZRR53quF',
        'client_secret': 'test_key',
    }

    return render(request, template, context)
