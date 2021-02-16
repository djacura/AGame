from django.urls import path
from .views import (
    MembershipSelectView,
    PaymentView,
    updateTransactions,
    cancelsubscription,
)

app_name = 'memberships'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select_membership'),
    path('payment/', PaymentView, name='payment'),
    path('update_transactions/<subscription_id>',
         updateTransactions, name='update_transactions'),
    path('cancel/', cancelsubscription, name='cancel'),
]
