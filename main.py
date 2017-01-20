import time
from copy import deepcopy
import random
import signal
from Board import Board 
from Gameplay import GamePlay

class _GetchUnix:
    def __init__(self):
        import tty, sys 

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def inp(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = abc()
        signal.alarm(0)
        return text
    except AlarmException:
        print ''
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
game=GamePlay()




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
                



blocks=[Block([[1,0],[1,1],[1,2],[1,3]]),Block([[1,0],[1,1],[2,0],[2,1]]),Block([[1,0],[1,1],[2,1],[2,2]]),Block([[1,1],[1,2],[2,0],[2,1]]),Block([[1,0],[1,1],[1,2],[2,2]]),Block([[1,1],[2,0],[2,1],[2,2]]),Block([[1,1],[1,1],[1,1],[1,1]])]

cur_block=Block(deepcopy(blocks[2].retBlock())) 

free=1
started=0
abc=_GetchUnix()
while 1:
        
        cur=deepcopy(cur_block.retBlock())   
        for j in range(0,4):
            game.emptyBoard(cur[j])
        for j in range(0,4):
                
                if game.checkPoint(cur[j][0]+1,cur[j][1])==0 and started==1:
                    for i in range(0,4):
                                game.fillBoard(cur[i])
                    if a==6 and j!=32:
                        for i in range(1,31):
                            game.fillBoard([cur[j][0],i])
                        game.rowsFull()
                        game.updateScore(100)
                                
                    free=1
                    game.updateScore(10)
                    break

        if free:
            
                a=game.selectBlock()
                if a==19 :
                    a=6
                else:
                    a=a%6
                temp=deepcopy(blocks[a].retBlock())
                if game.gameOver(temp):
                        print "GAME OVER"
                        break
                for j in range(0,4):
                        temp[j][1]+=15
                        game.fillBoard(temp[j])
                
                cur_block.update(temp)
                started=1
                game.randRow()
            
               
       
      
       
        ch=''
        ch=inp()
        cur_block.moveDown()
        if ch=='a' or ch=='A': 
                #left
                OK=1
                for j in range(0,4):
                        if game.checkPoint(cur[j][0],cur[j][1]-1)==0:
                                OK=0
                if OK:
                
                        cur_block.moveLeft()
        if ch=='d' or ch=='D': 
                 #right
                OK=1
                for j in range(0,4):
                        if game.checkPoint(cur[j][0],cur[j][1]+1)==0:
                                OK=0
                if OK:
                        cur_block.moveRight()
                                

        if ch==' ':
               
                cur_block.fullDown()

        if ch=='w' or ch=='W':
            cur_block.rotate()
                        
        cur=deepcopy(cur_block.retBlock())  
        for j in range(0,4):
            game.fillBoard(cur[j])
        game.printBoard()
        game.rowsFull()
        free=0
        print "\n\n\n"
        
		
	

