import time
from copy import deepcopy
import random
import signal

class Board:
        
        def __init__(self):
                self.board=[]
                borderrow=[]
                for i in range(0,32):
                        borderrow.append(".")
                self.board.append(borderrow)
                for i in range(0,32):
                        row=["."]
                        for j in range(0,30):
                                row.append(" ")

                        row.append(".")
                        self.board.append(row)

                self.board.append(borderrow)
                no=random.randint(0,4)
                for j in range(0,no):
                    x=random.randint(0,25)
                    y=random.randint(5,30)
                    for i in range (x,x+5):
                        self.board[y][i]="*"

        def checkPoint(self,pointX,pointY):
                if self.board[pointX][pointY]!=' ':
                        return 0
                return 1

        
        def fillBoard(self,point):
                self.board[point[0]][point[1]]="X"
         
        def emptyBoard(self,point):
                self.board[point[0]][point[1]]=" "

                
                
