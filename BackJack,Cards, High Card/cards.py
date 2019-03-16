class Card(object):
    """A playing card.
    this class will build a single card
    to build a card call card() and pass in a rnak and a suit
    card1= Card(rank="A",suit="s")"""

    RANKS=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    SUITS=['♠','♥','♦','♣']

    def __init__(self,rank,suit,face_up=True):
        self.rank=rank
        self.suit=suit
        self.is_face_up=face_up

    def __str__(self):
        if self.is_face_up:
            rep=self.rank+self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    """A hand of playing cards.
    Clear clears all the cards in your hand
    To check if clear works you do my_hand.clear() then print it to see if it clears
    Add adds cards to your hand
    To add a card my_hand.add(card)
    give card gives a card to the other append
    to give a card give(card,other_hand)
    """
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep+=str(card)+" "
        else:
            rep="<empty>"
        return rep

    def clear(self):
        self.cards=[]

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """A deck of playing cards.
    deck=Deck()"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")

if __name__=="__main__":
    print("You ran this module directly(and did not 'import' if).")
    input("Press the enter key to exit.")
