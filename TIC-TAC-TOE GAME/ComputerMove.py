from random     import randrange
from FreeFields import listOfFreeFields


def computerMove(board):
    free = listOfFreeFields(board)
    count = len(free)
    if(count>0):      #this function is related to computers move the computer randomly put symbol into the table
       point = randrange(count)
       row,col = free[point]
       board[row][col] = 'X'

