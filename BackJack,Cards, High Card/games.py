import cards
# from 5 different codes
#-2
def ask_yes_no(question):
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response
#-1
def ask_num(question, low, high):
    """Ask for number
    what the question is that you want to ask
    the low number
    the high number"""
    while True:
        num = input(question + "("+str(low) + "," + str(high)+"):")
        try:
            low = int(low)
            high = int(high)
            num = int(num)
            if num in range(low, high+1):
                return num
            print("Oops! That was not the number we were looking for. Try again...")
        except:
            print("Oops! That was not the number we were looking for. Try again...")
            pass

def switch_turn(num_players,turn):
    """switch turns
    import how many players there are
    turn=0"""
    turn=turn
    if turn < num_players - 1:
        turn+=1
    else:
        print("")

def winner_grats(player):
    print(player,"You Won Good Job")
    input("Press enter to Exit")
    pass

class Player(object):
    def __init__(self,name,score):
        self.name=name
        self.score=str(self.score)
    def __str__(self):
        rep=self.name
        rep=rep+" "+str(score)

if __name__=="__main__":
    print("You ran this module directly(and did not 'import' if).")
    input("Press the enter key to exit.")
