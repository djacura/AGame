from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from memberships.views import (
    get_user_membership,
    get_selected_membership,
    get_user_subscription
)


@login_required
def profile(request):
    """
    Displays the Users Profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)

    if request.user.is_authenticated:
        current_membership = get_user_membership(request)
        current_membership = str(current_membership.membership)

    else:
        current_membership = False

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'user_membership': user_membership,
        'user_subscription': user_subscription,
        'current_membership': current_membership,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
