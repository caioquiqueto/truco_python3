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

        self.table = Table()

        self.UsScore = 0
        self.theyScore = 0

    def StartMatch(self):
        self.player1.SetName(input("qual o nome do Jogar 1"))
        self.player2.SetName(input("qual o nome do Jogar 2"))
        self.player3.SetName(input("qual o nome do Jogar 3"))
        self.player4.SetName(input("qual o nome do Jogar 4"))
        
        self.table.SetTable(self.player1,self.player2,self.player3,self.player4)
#Classe que controla a rodada
#class Set():

#Classe que controla a mão
#class Game():

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

    def GetGreatestCardIndex(self,vira):
        for card in self.hand:
            if GreatestCard :
                GreatestCard = card
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

        self.cardTurn = Deck.Card()

    def SetTable(self,ps,pe,pn,pw):
        self.southSit.SetPlayer(ps)
        self.eastSit.SetPlayer(pe)
        self.northSit.SetPlayer(pn)
        self.westSit.SetPlayer(pw)

        self.deck.BuildDeck()
        self.deck.ShuffleDeck()

        for nX in range(0,2):
            ps.ReciveCard(self.deck.GetCard())
            pe.ReciveCard(self.deck.GetCard())
            pn.ReciveCard(self.deck.GetCard())
            pw.ReciveCard(self.deck.GetCard())

        self.cardTurn = self.deck.GetCard()

#Classe que controla o assento do jogador
class Sit():
    def __init__(self):
        self.player = Player()
        self.isDealer = False

    def SetPlayer(self, player):
        self.player = player

    def setDealer(self, isDealer):
        self.isDealer = isDealer

print("que comessem os jogos!!!!")
myMatch = Match()

myMatch.StartMatch()