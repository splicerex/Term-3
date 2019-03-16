import time

class Critter(object):

    def __init__(self,name,hunger=0,boredom=0):
        self.name = name
        self.__hunger = hunger
        self.__boredom = boredom
        
    def __pass_time(self):
        self.__hunger+=1
        self.__boredom+=1

    @property
    def mood(self):
        unhappiness = self.__hunger + self.__boredom
        if unhappiness < 5:
            mood="Happy"
        elif 5<= unhappiness <10:
            mood="Okay"
        elif 10<= unhappiness <15:
            mood="Frustrated"
        else:
            mood="Mad Mad"
        return mood

    def food_boredom(self):
        if 0 <= self.__hunger < 3:
            food="Full"
        elif 3 <= self.__hunger < 6:
            food="Hungry"
        elif 6 <= self.__hunger < 9:
            food = "Very Hungry"
        elif 9 <= self.__hunger :
            food = "Starving"
        if 0 <= self.__boredom < 3:
            bored="Having fun"
        elif 3 <= self.__boredom < 6:
            bored="Bored"
        elif 6 <= self.__boredom < 9:
            bored="Very Bored"
        elif 6 <= self.__boredom :
            bored="Deathly Bored"
        return food , bored

    def play(self,fun=4):
        print("Wheeee")
        self.__boredom-=fun
        if self.__boredom<0:
            self.__boredom = 0
        self.__pass_time()

    def talk(self):
        mood=self.mood
        food,bored=self.food_boredom()
        print(self.name,"My mood is",mood)
        print(self.name,"My hunger is",food)
        print(self.name, "is", bored)
        self.__pass_time()


    def eat(self,food=4):
        print("Brruppp. Thanks")
        self.__hunger-=food
        if self.__hunger < 0:
            self.__hunger=0
        self.__pass_time()


def main():
    crit_name=input("What is your critters name?")
    crit=Critter(crit_name)
    #create critter
    choice=None
    while choice !=0:
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        choice=input("Choice:")
        print()
        #exit
        if choice=="0":
            print("Goodbye")
            break
        elif choice=="1":
            crit.talk()
        elif choice=="2":
            crit.eat()
        elif choice=="3":
            crit.play()
        else:
            print("Not a good choice")
main()
input("Press the enter key to exit")



            
