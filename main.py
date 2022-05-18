
from abc import ABC, abstractmethod
import random

moves = ['rock','paper','scissor']
mapping = {'r':0 , 'p' : 1 , 's' : 2}

class Strategy :    # interface
    @abstractmethod
    def makemove(self,lasthumanmove):
        pass


class MirrorMove(Strategy) :    # concrete strategy 1
    def makemove(self,lasthumanmove):
        return lasthumanmove


class RandomMove(Strategy) :    # concrete strategy 2
    def makemove(self,lasthumanmove):
        return random.randint(0,2)

class Computer :

    def __init__(self):
        self.strategy = RandomMove()
        self.lasthumanmove = 0
        self.human = 0
        self.computer = 0

    def setStrategy(self , arg):
        if arg == 1 :
            self.strategy = RandomMove()
        else :
            self.strategy = MirrorMove()

    def makemove(self, lasthumanmove, curhumanmove):
        return self.strategy.makemove(lasthumanmove)

    def update(self,curcompmove,curhumanmove):
        if curcompmove == (curhumanmove + 1) % 3 :
            self.computer += 1
        elif curcompmove != curhumanmove :
            self.human += 1

        self.lasthumanmove = curhumanmove

        print('Computer played : {}'.format(moves[curcompmove]))
        print('Scores : \nComputer : {}\t\t\t You : {}\n'.format(self.computer,self.human))

    def playTurn(self,lasthumanmove,curhumanmove):
        curcompmove = self.makemove(lasthumanmove,curhumanmove)
        self.update(curcompmove,curhumanmove)


comp = Computer()

print("You are playing Rock-Paper-Scissors against Computer.")
print("Enter key as per : ")
for i,c in zip(range(3),mapping.keys()) :
    print('{} for {}'.format(c,moves[i]))
print("To switch computer playing strategy, type :")
print('- M for mirrorMove. \n- R for randomMove.')


# game loop
while True :
    c = input('Enter your choice : ')
    try :
        assert c in ['r','p','s','M','R']
    except Exception as e :
        print('Enter a letter from [r,p,s,R,M] only.')
        continue

    if c == 'M' :
        comp.setStrategy(MirrorMove())
    elif c == 'R' :
        comp.setStrategy(RandomMove())
    else :
        comp.playTurn(comp.lasthumanmove,mapping[c])





