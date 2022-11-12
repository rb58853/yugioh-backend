from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView
from rest_framework.response import Response
from ..domain.queries import TournamentQueries, MatchQueries
from ..usecases.round import RoundUseCases
from apps.users.interfaces.serializers import PlayerSerializer
from .serializers import (TournamentSerializer, RegistertSerializer,
                          RoundSerializer) 



class TournamentCreateView(CreateAPIView):
    serializer_class  = TournamentSerializer

    def perform_create(self, serializer):
        data = serializer.data
        finish_date = data.get('finish_date', None)
        address = data.get('address', None)
        TournamentQueries().create(name=data['name'], manager= data['manager'],
                                   address=address)
        

class ParticipantCreateView(CreateAPIView):
    serializer_class  = RegistertSerializer

    def perform_create(self, serializer):
        data = serializer.data
        TournamentQueries().register_players(tournament_id=data['tournament_id'],
                                             players_info=data['players'])


class RoundCreateView(CreateAPIView):
    serializer_class  = RoundSerializer

    def perform_create(self, serializer):
        data = serializer.data
        RoundUseCases().create(name=data['name'],tournament_id=data['tournament_id'])

class Champion(RetrieveAPIView): 
    serializer_class = PlayerSerializer
    
    def retrieve(self, request, *args, **kwargs):
        tournament_id = request.query_params.get('tournament_id',0)
        self.queryset = TournamentQueries.champion(tournament_id)        
        serializer = self.get_serializer(self.queryset)
        return Response(serializer.data)
    
class MoreVictories(RetrieveAPIView): 
    # serializer_class = PlayerSerializer
    
    def retrieve(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date',0)
        end_date = request.query_params.get('end_date',0)
        self.queryset = TournamentQueries.more_victories(start_date,end_date)        
        # serializer = self.get_serializer(self.queryset)
        return Response(self.queryset)
    
class Archetype_More_Used(RetrieveAPIView): 
    
    def retrieve(self, request, *args, **kwargs):
        tournament_id = request.query_params.get('tournament_id',0)
        self.queryset = TournamentQueries.archetype_more_used(tournament_id)        
        # serializer = self.get_serializer(self.queryset)
        return Response(self.queryset)

class ChampionsArchetypes(RetrieveAPIView): 
    
    def retrieve(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date',0)
        end_date = request.query_params.get('end_date',0)
        self.queryset = TournamentQueries.champions_archetypes(start_date,end_date)        
        # serializer = self.get_serializer(self.queryset)
        return Response(self.queryset)
    
    
class PlaceWithMoreChampions(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date',0)
        end_date = request.query_params.get('end_date',0)
        self.queryset = TournamentQueries.place_with_more_champions(start_date,end_date)        
        # serializer = self.get_serializer(self.queryset)
        return Response(self.queryset)

