from django.shortcuts import render
from django.http import JsonResponse
from ..tournament.data.models import Match, Participant, Tournament, Round
from ..users.data.models import Player
from ..ygo.data.models import Deck

def players(request):
    data  = list(Player.objects.values())
    return JsonResponse(data,safe = False)

def tournaments(request):
    data  = list(Tournament.objects.values())
    return JsonResponse(data,safe = False)

def decks(request):
    data  = list(Deck.objects.values())
    return JsonResponse(data,safe = False)

def rounds(request):
    data  = list(Round.objects.values())
    return JsonResponse(data,safe = False)

def matchs(request):
    data  = list(Match.objects.values())
    return JsonResponse(data,safe = False)

def participants(request):
    data  = list(Participant.objects.values())
    return JsonResponse(data,safe = False)
