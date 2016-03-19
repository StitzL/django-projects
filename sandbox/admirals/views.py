from django.shortcuts import render, get_object_or_404, redirect
import random, string, json, requests
from django.http import JsonResponse
from django.template.context_processors import csrf

def index(request):
	c = {"action":"It's good that you have come."}
	c.update(csrf(request))
	return render(request, 'admirals/index.html', c)

	
def new_game(request):
	player = request.POST.get("player", "")
	if (player == ''):
		return JsonResponse({'error': "You must take personal responsibility here. Let our sailors know who you are, and the the enemy who they are dealing with."})
	game = next_game_id
	c = {"player": player, "action": "Game started", "game": game}
	c.update(csrf(request))
	print("New game, player " + player)
	return render(request, 'admirals/board.html', c)
	
def game(request):
	c = {"player": player, "action": "Game started", "game": game}
	c.update(csrf(request))
	return render(request, 'admirals/board.html', c)

def next_game_id(): 
	return 4711