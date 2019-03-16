#Kyle Baldiwn
#3/7/19
#Typer

#imports
import time as T
import math as M
import os
import sys

#Classes
class Money(object):
    def __init__(self):
        self.money=0
        self.money_per = .01
        self.timer = 10000
class Buy(object):
    def __init__(self):
        self.fast_key = 10
        self.keyboard = 20
        self.keys = 30
        self.fast_time = 40
        self.two_time=50
        self.three_time=60
        self.four_time=70
        self.shop_keyboard=100
        self.factory_keyboard=200
        self.world_keyboard=300
        self.galaxy_keyboard=400
        self.time_travel=500
        self.time_drift=600

#functions
def buy(cost,item,add,self):
    self.money_per+=add
    print("You have purchased",item,"now you make",str(self.money_per),"per second")
    self.money-=cost
    print("Your money is now",self.money)
    T.sleep(3)

def time(cost,item,add,self):
    self.timer -=add
    print("You have purchased", item, "now you're auto typer will run fast")
    self.money -= cost
    print("Your money is now",self.money)
    T.sleep(3)

def buy_menu(self):
    self2=Buy()
    while True:
        print("This is the market.\nTo buy you type the number in front of what you want to buy.\n\n1:Fast Keys \nCost:",self2.fast_key,"\n\n2:Keyboard +1\nCost:",self2.keyboard,
              "\n\n3:Keys\nCost:",self2.keys,"\n\n4:Fast Time\nCost:",self2.fast_time,"\n\n5:2x Speed\nCost:",self2.two_time,"\n\n6:3x Speed\nCost:",self2.three_time,"\n\n7:4x Speed\nCost:",self2.four_time,
              "\n\n8:KeyBoard Store\nCost:",self2.shop_keyboard,"\n\n9:KeyBoard Factory\nCost:",self2.factory_keyboard,"\n\n10:KeyBoard World\nCost:",self2.world_keyboard,"\n\n11:KeyBoard Galaxy\nCost:",self2.galaxy_keyboard,
              "\n\n12:Time Travel\nCost:",self2.time_travel,"\n\n13:Time Drift\nCost:",self2.time_drift,
              "\n\nExit press enter\n")
        purchased=input("What would you like to buy?")
        if purchased=="1":
            if self.money >= self2.fast_key:
                buy(self2.fast_key,"Fast Keys",.5,self)
                self2.fast_key+=10
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="2":
            if self.money >= self2.keyboard:
                buy(self2.keyboard,"Keyboard", .10,self)
                self2.keyboard+=20
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="3":
            if self.money>=self2.keys:
                buy(self2.keys,"keys",.20,self)
                self2.keys+=30
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="4":
            if self.money>=self2.fast_time:
                time(self2.fast_time,"Faster Timer",1,self)
                self2.fast_time+=40
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="5":
            if self.money>=self2.two_time:
                time(self2.two_time,"2x speed",20,self)
                self2.two_time+=50
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="6":
            if self.money>=self2.three_time:
                time(self2.three_time,"3x Speed",30,self)
                self2.three_time+=60
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="7":
            if self.money>=self2.four_time:
                time(self2.fast_time,"4x Speed",40,self)
                self2.four_time+=70
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="8":
            if self.money>=self2.shop_keyboard:
                buy(self2.shop_keyboard,"Keyboard Store",1,self)
                self2.shop_keyboard+=100
            else:
                print("You do not have enough money")
                T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="9":
           if self.money>=self2.factory_keyboard:
               buy(self2.factory_keyboard,"KeyBoard Factory",2,self)
               self2.factory_keyboard+=200
           else:
               print("You do not have enough money")
               T.sleep(3)
           clear = lambda: os.system('cls')
           clear()
        elif purchased=="10":
            if self.money>=self2.world_keyboard:
               buy(self2.world_keyboard,"KeyBoard World",3,self)
               self2.world_keyboard+=300
            else:
               print("You do not have enough money")
               T.sleep(3)
            clear = lambda: os.system('cls')
            clear()
        elif purchased=="11":
           if self.money>=self2.galaxy_keyboard:
               buy(self2.galaxy_keyboard,"KeyBoard Galaxy",4,self)
               self2.galaxy_keyboard+=400
           else:
               print("You do not have enough money")
               T.sleep(3)
           clear = lambda: os.system('cls')
           clear()
        elif purchased=="12":
           if self.money>=self2.time_travel:
               time(self2.time_travel,"Time Travel",100,self)
               self2.fast_time+=500
           else:
               print("You do not have enough money")
               T.sleep(3)
           clear = lambda: os.system('cls')
           clear()
        elif purchased=="13":
           if self.money>=self2.time_drift:
               time(self2.time_drift,"Time Drift",1000,self)
               self2.time_drift+=600
           else:
               print("You do not have enough money")
               T.sleep(3)
           clear = lambda: os.system('cls')
           clear()
        elif purchased=="":
            clear = lambda: os.system('cls')
            clear()
            break
        else:
            print("This is not an opion")
            T.sleep(3)
            clear = lambda: os.system('cls')
            clear()

def typer(self):
    while True:
        type=input("Type anything to make money.\nIf you want to stop typing type menu").lower()
        if type=="menu":
            break
        else:
            self.money+=self.money_per
            self.money=M.ceil(self.money*100)/100
            print(self.money)
            clear = lambda: os.system('cls')
            clear()


def auto_typer(self):
    while True:
        print("This will run every",str(self.timer),"seconds\nPress enter to exit")
        i=input("How long do you want to run this?")
        if i=="":
            break
        for l in range(int(i)):
            self.money+=self.money_per
            self.money = M.ceil(self.money * 100) / 100
            T.sleep(int(timer))
            l+=1
            print(self.money)

def main():
    self=Money()
    print("Welcome to Keyboard Typer.\nThis is a game that you make money by typing simple enough.")
    print("Type a number to go where you want to go")
    while True:
        i=input("1 Buy Menu\n2 Money Making\n3 Auto Money Making\nPress Enter To Exit.")
        if i=="1":
            buy_menu(self)
        elif i=="2":
            typer(self)
        elif i=="3":
            auto_typer(self)
        elif i=="":
            print("Thanks for playing hope you had fun Goodbye")
            sys.exit()
        elif i=="Kyle Baldwin":
            self.money+=100000
            print("Cheats On")

main()

#money=Money()
#print(money.money)




