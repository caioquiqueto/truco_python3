#fonte responsavel por controlar a partida
import Deck
"""

 ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌
▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ▐░▌       ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀         ▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
                                                                 
                                      
"""
#Classe que controla a partida
class Match ():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player3 = Player()
        self.player4 = Player()

        self table = Table()

#Classe que controla a rodada
class Set():

#Classe que controla a mão
class Game():

#Classe que controla o jogador
class Player():
    def __init__(self):
        self.name = ''
        self.hand = []

    #metodos de controle do nome
    def SetName(self,name):
        self.name = name
    def Getname(self):
        return self.Getname

    #metodos de controle da mão do jogador
    def ReciveCard(self,card):
        self.hand.append(card)

    def SendCard(self,index):
        return self.hand.pop(index)

    def GetGreatestCardIndex(self,vira)
        for card in self.hand:
            if GreatestCard :
                
            else:
                GreatestCard = card
        return GreatestCard


#Classe que controla a mesa do jogo
class Table():
    def __init__(self):
        self.southSit = Sit()
        self.eastSit = Sit()
        self.northSit = Sit()
        self.westSit = Sit()

        self.deck = Deck.Deck()

    def SetTable(self,ps,pe,pn,pw):
        self.southSit.SetPlayer(ps)
        self.eastSit.SetPlayer(pe)
        self.northSit.SetPlayer(pn)
        self.westSit.SetPlayer(pw)

        self.deck.BuildDeck()
        self.deck.ShuffleDeck()

#Classe que controla o assento do jogador
class Sit():
    def __init__(self):
        self.player = Player()
        self.isDealer = False

    def SetPlayer(self, player):
        self.player = player

    def setDealer(self, isDealer):
        self.isDealer = isDealer