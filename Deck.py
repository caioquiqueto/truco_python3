#python 3.6
#meu programa de truco
from random import randint
"""

 ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌ 
▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▐░▌  
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌░▌   
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░▌    
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌░▌   
▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌▐░▌  
▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌ 
▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌
 ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀ 
                                               
"""

class Deck():
    def __init__(self):
        self.deck = []
        #♠♣♥♦
        self.suits= ["♣","♥","♠","♦"]
        self.ranks=["A","2","3","4","5","6","7","Q","J","K"]

    def BuildDeck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit,rank))

    def ShowDeck(self):
        for card in self.deck:
            print(card.GetSuit() + card.GetRank())

    def ShuffleDeck(self):
        newDeck = []
        #cloneDeck = self.deck.copy()
        for nX in range(39,0,-1):
            newDeck.append(self.deck.pop(randint(0,nX)))
        self.deck = newDeck.copy()

    def GetCard(self):
        return self.deck.pop

class Card():
    def __init__(self,suit="",rank=""):
        self.suit=suit
        self.rank=rank
        self.manilha=False

    def GetSuit(self):
        return self.suit

    def GetRank(self):
        return self.rank

def CompareCard(card1,card2,turn):
    rankOrder = GetRankOrder(turn)
    suitOrder = GetSuitOrder()
    rankindex1 = card1.GetRank()
    rankindex2 = card2.GetRank()

    """
    if rankindex1 = rankindex2:
        
    else:
        if rankindex1 > rankindex2:
            card = card1
        else:
            card = card2

    return card"""

def GetRankOrder(turn = "2"):
    rankOrder = ["4","5","6","7","Q","J","K","A","2","3"]
    if turn == "3":
        rankOrder.append(rankOrder.pop(0))#vai pegar o 4
    else:
        rankOrder.append(rankOrder.pop(rankOrder.index(turn) + 1))

    return rankOrder

def GetSuitOrder():
    return ["♦","♠","♥","♣"]