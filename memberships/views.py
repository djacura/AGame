from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Membership, UserMembership, Subscription

import stripe


def get_user_membership(request):
    """gets the users current membership (Logic and code by Mat @ JustDjango).
    Understood and implemented."""

    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    """Gets the subcription name (Logic and code by Mat @ JustDjango).
    Understood and implemented."""

    user_membership_qs = UserMembership.objects.filter(user=request.user)
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def get_selected_membership(request):
    """Gets the membership type from the session
    Understood and implemented.(Logic and code by Mat @ JustDjango)."""

    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None


class MembershipSelectView(ListView):
    """List the selected membership (Logic and code by Mat @ JustDjango).
    Understood and implemented."""

    model = Membership

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self, request, **kwargs):
        selected_membership_type = request.POST.get('membership_type')
        user_membership = get_user_membership(request)
        user_subscription = get_user_subscription(request)
        selected_membership_qs = Membership.objects.filter(
            membership_type=selected_membership_type)
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()

        """ VALIDATION """

        if user_membership.membership == selected_membership:
            if user_subscription != None:
                messages.info(request, "You have this membership. Your \
                    next payment is due {}".format('get this from stripe'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        request.session['selected_membership_type'] = selected_membership.membership_type

        return HttpResponseRedirect(reverse('memberships:payment'))


def PaymentView(request):
    """Provide user with payment form and payment
    (Logic and code by Mat @ JustDjango). Understood and implemented."""

    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)

    publicKey = settings.STRIPE_PUBLIC_KEY

    context = {
        'publicKey': publicKey,
        'selected_membership': selected_membership
    }

    return render(request, 'memberships/membership_payment.html', context)
