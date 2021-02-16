from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Game
from .forms import GameForm
from memberships.views import (
    get_user_membership,
    get_selected_membership,
    get_user_subscription
)


def all_games(request):
    """ A view to show and search for Games """

    games = Game.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('games'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'games/games.html', context)


def game_detail(request, game_id):
    """ A view to see the Game detail page """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }

    return render(request, 'games/game_detail.html', context)


@login_required
def add_game(request):
    """ Add a Game to the website """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            messages.success(request, 'Successfully added Game!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(request, 'Failed to add Game! Please ensure the form is valid!')
    else:
        form = GameForm()

    form = GameForm()
    template = 'games/add_game.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_game(request, game_id):
    """ Edit a Game on the website """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Game!')
            return redirect(reverse('game_detail', args=[game.id]))
        else:
            messages.error(request, 'Failed to update Game! Please ensure the form is valid!')
    else:
        form = GameForm(instance=game)
        messages.info(request, f'You are editing {game.name}')

    template = 'games/edit_game.html'
    context = {
        'form': form,
        'game': game,
    }

    return render(request, template, context)


@login_required
def delete_game(request, game_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    game = get_object_or_404(Game, pk=game_id)
    game.delete()
    messages.success(request, 'Game deleted!')
    return redirect(reverse('games'))
