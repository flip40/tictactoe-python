from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Game
import json

def index(request):
    return render(request, 'index/base.html')
    #return HttpResponse("hallo!", content_type="text")

def get_games(request):
    data = serializers.serialize("json", Game.objects.all().filter(players=1).filter(leaver=False))
    data = json.loads(data)
    games = []
    for game in data:
        fields = game['fields']
        fields['pk'] = game['pk']
        games.append(fields)
    return HttpResponse(json.dumps(games), content_type="application/json")

def get_game(request):
    data = serializers.serialize("json", Game.objects.all().filter(pk=request.GET.get('id')))
    data = json.loads(data)[0]
    game = data['fields']
    game['pk'] = data['pk']
    game['gamestate'] = json.loads(game['gamestate'])
    return HttpResponse(json.dumps(game), content_type="application/json")

def create_game(request):
    game = Game.objects.create(name=request.GET.get('name', 'Unnamed Game'), player1=request.GET.get('player', 'Nony Mouse'), gamestate='[["", "", ""], ["", "", ""], ["", "", ""]]', turn='X', players=1, leaver=False, winner="", draw=False)
    game.save()
    return HttpResponse(json.dumps({'created': True, 'gameid': game.pk, 'token': 'X'}), content_type="application/json")

def join_game(request):
    game_entry = Game.objects.get(pk=request.GET.get('id'))
    game_entry.players += 1
    if game_entry.players == 2 and game_entry.leaver == False:
        game_entry.player2 = request.GET.get('name', 'Nony Mouse')
        game_entry.save()
        return HttpResponse(json.dumps({'joined': True, 'token': "O"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'joined': False}), content_type="application/json")

def leave_game(request):
    game = Game.objects.get(pk=request.GET.get('id'))
    game.leaver = True
    game.save()
    #game.players -= 1
    #game.save()
    return HttpResponse(json.dumps({'left': True}), content_type="application/json")

def take_spot(request):
    gameid = request.GET.get('id', None)
    row = int(request.GET.get('row', None))
    column = int(request.GET.get('column', None))
    player = request.GET.get('token', None)
    if gameid is not None and row is not None and column is not None and player is not None:
        game = Game.objects.get(pk=gameid)
        board = json.loads(game.gamestate)
        if game.turn == player and board[row][column] == "":
            board[row][column] = player
            for row in board:
                if all([spots == player for spots in row]):
                    game.winner = player
            for column in range(0,3):
                if all([row[column] == player for row in board]):
                    game.winner = player
            if all([board[i][i] == player for i in range(0,3)]):
                game.winner = player
            if all([board[2-i][i] == player for i in range(0,3)]):
                game.winner = player
            if len([row for row in board if "" in row]) == 0:
                game.draw = True
            if player == "X":
                game.turn = "O"
            else:
                game.turn = "X"
            game.gamestate = json.dumps(board)
            game.save()
            return HttpResponse(json.dumps({'valid': True}), content_type="application/json")
    return HttpResponse(json.dumps({'valid': False}), content_type="application/json")

