from ..tournament.data.models import *

def arquetipes (idT, idR ):
    #Dado un torneo y una ronda, cuál o cuáles son los arquetipos más representados (cantidad de jugadores usándolos)
    _tournament = Tournament.objects.get(id = idT)
    _round = Round.objects.get(id = idR, tournament = _tournament)
    
    #matchs = _round.matchs()
    matchs =  Match.objects.filter(round = _round)

    arqList = []
    players = []
    
    for match in matchs :
        player1 = match.player1()
        player2 = match.player2()
        if players.__contains__(player1) == False : players.append(player1)
        if players.__contains__(player2) == False : players.append(player2)
    
    for player in players:
        inList = InList(player.deck.arquetipo,arqList)
        if inList[0]:
            i = inList[1]
            arqList[i][1] +=1
        else :
            arqList.append([player.deck.arquetipo,1])
    
    print(arqList)    
    # return arqList

def InList(arquetipo, arqList):
    i = 0
    for arq in arqList:
        if arq[0] == arquetipo:
            return [True, i]
        i+=1
    return [False, -1]