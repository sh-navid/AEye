# Reward
# Ponishment

import random

from enum import Enum


class Game:
    board = "#########"

    def check(self)->str: # X: Winner, O: Winner, C: Game is on, T: Tie
        b = self.board
        WIN=("123","456","789","147","258","369","159","357")
        for win in WIN:
            win=[int(x) for x in win]
            [c1,c2,c3]=win
            c1-=1
            c2-=1
            c3-=1

            if(b[c1]==b[c2] and b[c2] == b[c3] and b[c1]!="#"):
                return b[c1]
        
        if "#" in b:
            return "C"
        else:
            return "T"

    def show(self):
        co = 0
        for c in self.board:
            print(c, end="")
            print(" ", end="")
            co += 1
            if co % 3 == 0:
                print()

    def play(self,no,player):
        no-=1
        b=list(self.board)
        if(b[no]=="#"):
            b[no]=player
            self.board=b
            return True
        return False


class Agent:
    def __init__(self,name):
        self.name=name




matches=[]

for i in range(0,1000):
    g = Game()
    players=[Agent("X"),Agent("O")]
    while True:
        while True:
            r=random.choice([1,2,3,4,5,6,7,8,9])
            if(g.play(r,players[0].name)):
                break
        print("------")
        g.show()
        status=g.check()
        if(status in ["X","O","T"]):
            print(status)
            matches.append("".join(g.board)+">"+status)
            break
        players=players[::-1]

    print("################################################")

    print(matches)
    