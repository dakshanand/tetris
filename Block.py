import time
from copy import deepcopy
import random
import signal
from Board import Board 
from main import game

class Block():
        def __init__(self,block):
                 self.block=deepcopy(block)
                
                 
                         

        def retBlock(self):
                return self.block

        def update(self,block):
                self.block=block
                
        def moveDown(self):
                for j in range(0,4):
                        game.emptyBoard(self.block[j])
               
                        self.block[j][0]+=1
              
        def moveLeft(self):
                for j in range(0,4):
                        game.emptyBoard(self.block[j])
                        self.block[j][1]-=1
             

        def moveRight(self):
                for j in range(0,4):
                        game.emptyBoard(self.block[j])
                        self.block[j][1]+=1


        def fullDown(self):
                while 1 :
                        OK=1
                        for j in range(0,4):
                                if game.checkPoint(self.block[j][0]+1,self.block[j][1])==0:
                                        OK=0
                        if OK==0:
                                break
                                             

                        self.moveDown()

        def rotate(self):
           
            mincol,maxcol,minrow,maxrow=100,0,100,0
            for part in self.block:
                mincol=min(mincol,part[1])
                maxcol=max(maxcol,part[1])
                minrow=min(minrow,part[0])
                maxrow=max(maxrow,part[0])
            xc,yc=minrow,mincol
            xdim=maxrow-minrow+1
            ydim=maxcol-mincol+1
            initialblock=[[0 for y in range(ydim)] for x in range(xdim)]
            for part in self.block:
                initialblock[part[0]-xc][part[1]-yc]=1
  
            finalblock=zip(*initialblock[::-1])
            for i in range(ydim):
                finalblock[i]=finalblock[i]
            resultingblock=[]
            for i in range(ydim):
                for j in range(xdim):
                    if finalblock[i][j]==1:
                        resultingblock.append([xc+i,yc+j])
           
            OK=1
            for i in range(0,4):
                if self.checkPoint(resultingblock[i][0],resultingblock[i][1])==0:
                    OK=0
            if OK:
               
                self.block=resultingblock
                

