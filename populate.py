import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.development')

import django
django.setup()

from apps.ygo.data.models import Deck,Archetype
from apps.users.data.models import Player, User, Manager
from apps.tournament.data.models import Date, Participant, Tournament, Round, Match
from django.db.models import Count
import random
       
    
def run():
    
    for num in range(5):
        ua, created= User.objects.get_or_create(email="email{}".format(num), first_name="name{}".format(num),
                                            last_name="lt{}".format(num), username="{}".format(num))
        ua.save()
        ub, created= User.objects.get_or_create(email="email{}_{}".format(num,num), first_name="name{}_{}".format(num,num),
                                            last_name="lt{}_{}".format(num,num), username="{}_{}".format(num,num))
        ub.save()
        
        pl, created=  Player.objects.get_or_create( name="player{}".format(num), user=ua,  phone_number=num,
                          province= "P{}".format(num))
        pl.save()        
        pl1, created=  Player.objects.get_or_create( name="player{}_{}".format(num,num), user=ub,  phone_number=num*1000,
                          province= "P{}_{}".format(num,num))
        pl1.save()
        
        aaa, created =  Archetype.objects.get_or_create( name="a{}".format(num))
        aaa.save()
        
        dka, created = Deck.objects.get_or_create(name="Magos{}".format(num), player= pl, main_deck=3, extra_deck=2, 
                        side_deck=1, archetype= aaa)
        dka.save()
        dkb, created = Deck.objects.get_or_create(name="Magos{}_{}".format(num, num), player= pl1, main_deck=3, extra_deck=2, 
                        side_deck=1, archetype= aaa)
        dkb.save()
        # for i in range(5):
        #     if random.randint(1,10)> 5:
        #         dka, created = Deck.objects.get_or_create(name="Magos{}_{}".format(num,i), player= pl, main_deck=3, extra_deck=2, 
        #                 side_deck=1, archetype= aaa)
        #         dka.save()
        
        ma, created = Manager.objects.get_or_create(name="manager{}".format(num), user=ua)
        ma.save()
        
        da, created= Date.objects.get_or_create(date=datetime.date(2000+num, 1, 1))
        da.save()
        db, created= Date.objects.get_or_create(date=datetime.date(1900+num, 1, 1)) 
        db.save()
        
        ta, created= Tournament.objects.get_or_create(name="tournament{}".format(num),
                                                      start_date= datetime.date(2000+num, 1, 1),
                                                      finish_date=datetime.date(2000+num, 1, 1),
                                                      address = "D{}".format(num))
        t1, created= Tournament.objects.get_or_create(name="tournament{}_{}".format(num,num),
                                                      start_date= datetime.date(2000+num, 1, 1),
                                                      finish_date=datetime.date(2000+num, 1, 1),
                                                      address = "D{}".format(num))
        ta.save()
        ta.managers.add(ma)
        ta.save()
        
        ra, created= Round.objects.get_or_create(name="Ronda{}".format(num), tournament=ta)
        ra.save()
        
        pa, created= Participant.objects.get_or_create( tournament=ta,
                    registration_date=da, deck= dka, player= pl )
        pa.save()
        pb, created= Participant.objects.get_or_create(tournament=ta,
                    registration_date=db, deck= dkb, player= pl1 )  
        pb.save()
        
        pa1, created= Participant.objects.get_or_create( tournament=t1,
                    registration_date=da, deck= dka, player= pl )
        pa1.save()
        pb1, created= Participant.objects.get_or_create(tournament=t1,
                    registration_date=db, deck= dkb, player= pl1 )  
        pb1.save()

        mt, created= Match.objects.get_or_create( round=ra,  date=da,
                                player1=pa, player2=pb, winner=pb)
        mt.save()
        

