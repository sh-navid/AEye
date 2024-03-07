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

for i in range(0,30):
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

L1,L2,L3,L4,L5,L6=set(),set(),set(),set(),set(),set()
for m in matches:
    L1.add(m[0:2])
    L2.add(m[2:4])
    L3.add(m[4:6])
    L4.add(m[6:8])
    L5.add(m[8])
    L6.add(m[10])


L1,L2,L3,L4,L5,L6=tuple(L1),tuple(L2),tuple(L3),tuple(L4),tuple(L5),tuple(L6)
for i,m in enumerate(matches):
    printed=False

    try:
        print(L1[i],"   ",end="")
        printed=True
    except:
        print("  ","   ",end="")
    
    try:
        print(L2[i],"   ",end="")
        printed=True
    except:
        print("  ","   ",end="")
    
    try:
        print(L3[i],"   ",end="")
        printed=True
    except:
        print("  ","   ",end="")

    try:
        print(L4[i],"   ",end="")
        printed=True
    except:
        print("  ","   ",end="")
    
    try:
        print(L5[i],"   ",end="")
        printed=True
    except:
        print("  ","   ",end="")

    try:
        print(L6[i],"   ",end="")
        printed=True
    except:
        print("  ","   ",end="")


    

    print()

    if not printed:
        break
    