from ..data.models import Deck, DeckCards, Card, Archetype
from apps.users.domain.queries import PlayerQueries 
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.db import OperationalError
from itertools import chain

class DeckQueries():
    def gb_player(value_list, count_var ):
        """Grouped Deck by a variable and its accountant

        Args:
            values (string): variable for which to group 
            count_var (string): variable counter

        Returns:
            _type_: _description_
        """
        queryset=Deck.objects.all().values(value_list).annotate(amount=Count(count_var)).order_by('-amount')
        return queryset
    
    def create(self, name,player_id, main_deck, extra_deck, side_deck, cards):
        # TODO: Determinar arquetipo
        # arquetipo = find_archetype(cartas)
        player = PlayerQueries().get(player_id)
        archetype = ArchetypeQueries.get_archetype("a0")
        d, created = Deck.objects.get_or_create(name=name, player= player, main_deck=main_deck, extra_deck=extra_deck, 
                        side_deck=side_deck, archetype= archetype)
        
        if created is False:
            self.create_deck_card(d,cards)
    
    def create_deck_card(self, deck, cartas):
        return True
    
    def get_deck(id):
        return Deck.objects.get(id=id)
        
    
class ArchetypeQueries():
    def most_popular():
        queryset = Deck.objects.all().values('archetype').annotate(amount=Count('id')).order_by('-amount')
        return queryset
    
    # TODO: Use dynamic filters not to repeat method for province and municipality
    def most_popular_in_province(province):        
        queryset = Deck.objects.all().values('archetype').annotate(
            amount=Count('id')).filter(player__province= province).order_by('-amount')
        return queryset
    
    def most_popular_in_municipe(municipe):        
        queryset = Deck.objects.all().values('archetype').annotate(
            amount=Count('id')).filter(player__municipe= municipe).order_by('-amount')
        return queryset

    def get_archetype(archetype_name):
        try:
            archetype =Archetype.objects.get(name=archetype_name)
        except ObjectDoesNotExist:
            print("Either the archetype doesn't exist.")  
            archetype = None   
        except OperationalError:
            print("no such table: data_playe.")
            archetype = None   
        return archetype     
    
    def municipe_popular(archetype_id):
        queryset1 = Deck.objects.all().values('player__municipe').annotate(
            amount=Count('archetype')).filter(archetype_id= archetype_id).order_by('-amount').first()
        
        queryset = Deck.objects.all().values('player__province').annotate(
            amount=Count('archetype')).filter(archetype_id= archetype_id).order_by('-amount').first()
        return {"municipe": queryset1['player__municipe'], "province": queryset['player__province']}
          