from django.test import TestCase
from apps.ygo.data.models import Deck,Archetype, Player
from apps.users.models import Manager, User

from .models import Match, Round, Tournament, Date, Participant
from django.db.models import Count
import datetime
       
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
        
        ma, created = Manager.objects.get_or_create(name='luis', user=ua)
        mb, created = Manager.objects.get_or_create(name='Robert', user=ub)
        
        ta, created= Tournament.objects.get_or_create(name='Axie', managers=ma)
        tb, created= Tournament.objects.get_or_create(name='Yugioh', managers=mb)
        tc, created= Tournament.objects.get_or_create(name='Dota', managers=ma) 
        td, created= Tournament.objects.get_or_create(name='Ricon', managers=mb) 
        
        ra, created= Round.objects.get_or_create(name='Primera', tournament=ta)
        rb, created= Round.objects.get_or_create(name='Segunda', tournament=tb)
        rc, created= Round.objects.get_or_create(name='Tercera', tournament=tc)         
        
        da, created= Date.objects.get_or_create(date=datetime.date(2005, 1, 1))
        db, created= Date.objects.get_or_create(date=datetime.date(2006, 1, 1))
        dc, created= Date.objects.get_or_create(date=datetime.date(2007, 1, 1))
        dd, created= Date.objects.get_or_create(date=datetime.date(2008, 1, 1))  

        pa, created= Participant.objects.get_or_create(name='Primera', tournament=ta,
                    registration_date=da, deck= dka,player= plb )
        pb, created= Participant.objects.get_or_create(name='Segunda', tournament=tb,
                    registration_date=db, deck= dkb,player= plc)
        pc, created= Participant.objects.get_or_create(name='Tercera', tournament=tc,
                    registration_date=dc,deck= dkf,player= pla)
        
        ma, created= Match.objects.get_or_create(name='Primera', round=ra,  date=da,
                                player1=pla, player2=plc, winner=plc)
        mb, created= Match.objects.get_or_create(name='Segunda', round=rb, date=db,
                                player1=pla, player2=plc, winner=pla,)
        mc, created= Match.objects.get_or_create(name='Tercera',  round=rc, date=dc,
                                player1=pla, player2=plc, winner=pla,)        
        
        
    def test_winners_in_date():
        
        start_date = datetime.date(2005, 1, 1)
        end_date = datetime.date(2005, 3, 31)
        
        queryset= Match.objects.filter(pub_date__range=(start_date, end_date)).values(
                        'winner').annotate( Amount= Count('id')).order_by('-Amount')
        
        print(queryset)
        
        

