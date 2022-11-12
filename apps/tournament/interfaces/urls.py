from django.urls import path
from .views import (TournamentCreateView,ParticipantCreateView,
                    RoundCreateView, Champion,MoreVictories,
                    Archetype_More_Used,ChampionsArchetypes,
                    PlaceWithMoreChampions)

urlpatterns = [
   path('create/', TournamentCreateView.as_view()),
   path('register/', ParticipantCreateView.as_view()),
   path('round/create/', RoundCreateView.as_view()),
   path('champion/', Champion.as_view()),
   path('champion/date/', MoreVictories.as_view()),
   path('archetypes/used/', Archetype_More_Used.as_view()),
   path('archetypes/champions/', ChampionsArchetypes.as_view()),
   path('places/champions/', PlaceWithMoreChampions.as_view()),   
]