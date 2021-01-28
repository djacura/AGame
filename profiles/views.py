from django.shortcuts import render


def profile(request):
    """
    Displays the Users Profile
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
