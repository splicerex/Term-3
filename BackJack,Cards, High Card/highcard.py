import games,Cards
deck=Cards.Deck()
deck.populate()
deck.shuffle()
print("Welcome to the world's simplest game high card!")

again=None
while again !="n":
    players=[]
    num=games.ask_num(question="How many players?",low=2,high=11)
    for i in range(num):
        name=input("Player name: ")
        player=games.Player(name)
        players.append(player)
    hands=[]
    for player in players:
        hand = player.hand
        hands.append(hand)
    deck.deal(hands,1)
    print("Here are the game results:")
    for player in players:
        print(player)
    again=games.ask_yes_no("Do you want play again?(y/n)")
input("Press the enter key to exit")


