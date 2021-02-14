from django.urls import path
from . import views

urlpatterns = [
    path('', views.MembershipSelectView.as_view(), name='select_membership'),
]
