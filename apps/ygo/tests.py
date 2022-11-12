from django.test import TestCase
from apps.ygo.data.models import Deck,Archetype
from apps.users.data.models import Player, User
from django.db.models import Count
       
class DeckAgrupadosTestCase(TestCase):
    def setUp(self):
            
        ua, created= User.objects.get_or_create(email="loco", first_name="Emmanuel",
                                                last_name="Torres", username="4")
        ub, created= User.objects.get_or_create(email="loco", first_name="Emmanuel",
                                                last_name="Torres", username="41")
        uc, created= User.objects.get_or_create(email="loco", first_name="Emmanuel",
                                                last_name="Torres", username="42")  

        plb, created=  Player.objects.get_or_create(name="aa", user=ua, id="1", phone_number=123,
                              province= "PD")
        plc, created=  Player.objects.get_or_create(name="bb", user = ub, id="2", phone_number=123,
                               province= "SS")
        pla, created=  Player.objects.get_or_create( name="cc", user=uc, id="3", phone_number=123,
                               province= "SS")
        
        aaa, created =  Archetype.objects.get_or_create( name="a")
        bbb, created =  Archetype.objects.get_or_create( name="b")                    
        
        
        dka, created = Deck.objects.get_or_create(name="Magos", player= plb, main_deck=3, extra_deck=2, 
                            side_deck=1, archetype= aaa)
        dkb, created = Deck.objects.get_or_create(name="Zombies", player= plc, main_deck=3, extra_deck=2, #SS
                            side_deck=1, archetype= aaa)
        dkc, created = Deck.objects.get_or_create(name="Asesino", player= plc, main_deck=3, extra_deck=2, #SS
                            side_deck=1, archetype= aaa)
        dkd, created = Deck.objects.get_or_create(name="d", player= plb, main_deck=3, extra_deck=2,
                            side_deck=1, archetype= bbb)
        dke, created = Deck.objects.get_or_create(name="e", player= plc, main_deck=3, extra_deck=2, #SS
                            side_deck=1, archetype=bbb)
        dkf, created = Deck.objects.get_or_create(name="e", player= pla, main_deck=3, extra_deck=2, #SS
                            side_deck=1, archetype= aaa)        
        dkg, created = Deck.objects.get_or_create(name="e", player= plc, main_deck=3, extra_deck=2, #SS
                            side_deck=1, archetype=bbb)   
        

       

      
    def test_decks_populates(self):
        print("-----TEST 1: Deck more populated------\n")
        
        consulta = Deck.objects.all().values('player').annotate(
                    Amount= Count('id')).order_by('-Amount') 
        print(consulta)
        print("-----TEST 1 Correcto------\n")
           
    def test_archetype_by_place(self):
        print("-----TEST 2: Consulta Arquetipos por lugar------\n\n")
        
        consulta = Deck.objects.all().values('archetype').annotate(Amount=
            Count('id')).filter(player__province= 'SS').order_by('-Amount')
        self.assertEqual(consulta.get(archetype= 1), {'archetype': 1, 'Amount': 3})
        self.assertEqual(consulta.get(archetype= 2), {'archetype': 2, 'Amount': 2})
        print("-----TEST 2 Correcto------\n\n")
    
    def test_archetype_by(self):
        print("-----TEST 3: Consulta Arquetipos por lugar------ ]\n")
        
        consulta = Deck.objects.values_list('name', 'player')
                
        print("-----TEST 3 Correcto------\n\n")
        
        
        
        