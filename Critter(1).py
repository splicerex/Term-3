import time

class Critter(object):

    def __init__(self,name,hunger=0,boredom=0):
        self.name = name
        self.__hunger = hunger
        self.__boredom = boredom
        
    def __pass_time(self):
        self.hunger+=1
        self.boredom+=1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            mood="Happy"
        elif 5<= unhappiness <10:
            mood="Okay"
        elif 10<= unhappiness <15:
            mood="Frustrated"
        else:
            mood="Mad Mad"
        return mood

    def play(self,fun=4):
        print("Wheeee")
        self.boredom-=fun
        if self.bordom<0:
            self.boredom = 0
        self.__pass_time()

    def talk(self):
        mood=self.mood
        print(self.name,"My mood is",mood)
        self.__pass_time()


    def eat(self,food=4):
        while True:
            food_num=input("How much food do you want to feed your critter(1-10)")
            if food_num.isdigit():
                food=int(food_num)
                food=food_num
                print("Brruppp. Thanks")
                self.hunger-=food
                if self.hunger < 0:
                    self.hunger=0
                self.__pass_time()
            else:
                print("That is not a number")

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



            
