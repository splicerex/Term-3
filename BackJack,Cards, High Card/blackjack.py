#kyle baldwin
#2/15/19
#Blackjack

#import
import cards,games

#Classes
class BJ_Card(cards.Card):
    ACE_VALUE=1

    @property
    def value(self):
        if self.is_face_up:
            v=BJ_Card.RANKS.index(self.rank)+1
            if v > 10:
                v=10
        else:
            v=None
        return v
class BJ_Deck(cards.Deck):

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):

    def __init__(self,name):
        super(BJ_Hand,self).__init__()
        self.name=name

    def __str__(self,):
        rep=self.name+":\t"+super(BJ_Hand,self).__str__()
        if self.total:
            rep+="("+str(self.total)+")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t=0
        for card in self.cards:
            t+=card.value
        contains_ace=False
        for card in self.cards:
            if card.value==BJ_Card.ACE_VALUE:
                contains_ace=True
        if contains_ace and t<=11:
            t+=10
        return t
    def is_busted(self):
        return self.total > 21
class BJ_Player(BJ_Hand):
    def  is_hitting(self):
        response = games.ask_yes_no(self.name+",do you want a hit?(Y/N):")
        return response=="y"

    def bust(self):
        print(self.name,"busts.")
        self.lose()

    def lose(self):
        print(self.name,"loses.")

    def win(self):
        print(self.name,"wins.")

    def push(self):
        print(self.name,"pushes.")

class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total<17

    def bust(self):
        print(self.name,"bust.")

    def flip_first_card(self):
        first_card=self.cards[0]
        first_card.flip()

class BJ_Game(object):
    def __init__(self,names):
        self.players=[]
        for name in names:
            player=BJ_Player(name)
            self.players.append(player)
        self.dealer=BJ_Dealer("Dealer: Jeff")
        self.deck=BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp=[]
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
            return sp

    def __additional_cards(self,player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players+[self.dealer],per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
        if self.dealer.is_busted():
            for player in self.still_playing:
                player.win()
        else:
            for player in self.still_playing:
                if player.total>self.dealer.total:
                    player.win()
                elif player.total<self.dealer.total:
                    player.lose()
                else:
                    player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()

#Main
def main():
    print("Welcome to BlackJack!\n")
    names=[]
    number=games.ask_num("How many players!",low=1,high=8)
    for i in range(number):
        name=input("Enter player name: ")
        names.append(name)
    game=BJ_Game(names)
    again=None
    while again !="n":
        game.play()
        again=games.ask_yes_no("Do you want play again")
main()
input("Press the enter key to exit")