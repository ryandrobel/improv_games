from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game, User, Review

# Create your views here.
def games_index(request):

    context = {
        'all_games': Game.objects.all()
    }

    return render(request, 'games_index.html', context)

def add_a_game(request):

    return render(request, 'add_game.html')

def create_game(request):

    errors = Game.objects.basic_validator(request.POST)
    if len(errors) > 0 : 
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/games/add_game')

    else:
        Game.objects.create(
            game_name = request.POST['game_name'],
            number_of_players = request.POST['number_of_players'],
            instructions = request.POST['instructions'],
            creator = User.objects.get(id = request.session['user_id'])
        )

    return redirect('/games')

def view_game(request, game_id):

    context = {
        'game': Game.objects.get(id = game_id)
    }

    return render(request, 'view_game.html', context)

def edit_game(request, game_id):

    context = {
        'game': Game.objects.get(id = game_id)
    }

    return render(request, 'edit_game.html', context)

def update_game(request, game_id):
    errors = Game.objects.basic_validator(request.POST)
    if len(errors) > 0 : 
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f'/games/{game_id}/edit')

    else:
        game_changes = Game.objects.get(id = game_id)
        game_changes.game_name = request.POST['game_name']
        game_changes.number_of_players = request.POST['number_of_players']
        game_changes.instructions = request.POST['instructions']
        game_changes.save()

    return redirect('/games')

def delete_game(request, game_id):

    Game.objects.get(id = game_id).delete()
    return redirect('/games')
    




