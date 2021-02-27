from django.shortcuts import render
from memberships.views import get_user_membership


def index(request):
    """ A view to return the index page """

    if request.user.is_authenticated:
        current_membership = get_user_membership(request)
        current_membership = str(current_membership.membership)

    else:
        current_membership = False

    context = {
        'current_membership': current_membership,
    }

    return render(request, 'home/index.html', context)


def terms(request):

    return render(request, 'home/terms.html')
