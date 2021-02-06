from django.shortcuts import render, get_object_or_404
from .models import Game


def all_games(request):
    """ A view to show the Games """

    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'games/games.html', context)


def game_detail(request, game_id):
    """ A view to see the Game detail page """

    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }

    return render(request, 'games/game_detail.html', context)
