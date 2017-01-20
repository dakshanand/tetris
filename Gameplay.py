import time
from copy import deepcopy
import random
import signal
from Board import Board 


class GamePlay(Board):
        def __init__(self):
                Board.__init__(self)
                self.score=0

        def rowsFull(self):
                while 1:
                        end=1
                        for i in range(32,0,-1):
                                full=1
                                for j in range(1,31):
                                        if self.board[i][j]==' ':
                                                full=0

                                if full:
                                    self.score+=100
                                    temp=self.board[1]
                                    for k in range(1,31):
                                                self.board[i][k]=' '
                                    for j in range(1,i):
                                        temp1=self.board[j+1]
                                        self.board[j+1]=temp
                                        temp=temp1
                                    end=0
                                    break
                                        
                            
                                
                        if end:
                                break
        def updateScore(self,x):
                self.score+=x

        def retScore(self):
                return self.score

        def selectBlock(self):
                 a=random.randint(0,19)
                
                 return a

        def gameOver(self,cur_block):
                OK=0
                for j in range(0,4):
                        if self.checkPoint(cur_block[j][0],cur_block[j][1]+15)==0:
                                OK=1
                return OK

        def printBoard(self):
                for i in range(0,34):
                        print ''.join(self.board[i])

                print "SCORE: "+str(self.score)

        def randRow(self):
            chance=random.randint(1,6)
            if chance==1:
                row=['.']
                for i in range(0,31):
                    putX=random.randint(1,5)
                    if putX==1:
                        row.append("#")
                    else:
                        row.append(" ")
                row.append('.')
                for i in range(1,30):
                    temp=row[i]
                    j=32
                    while temp!=' ' and j:
                        temp1=self.board[j][i]
                        self.board[j][i]=temp
                        temp=temp1
                        j-=1
                        
                    
                

