from List_of_free_fields import listOfFreeFields
from random import randrange
def computerMove(board):
    free = listOfFreeFields(board)
    count = len(free)
    if(count>0):      #this function is related to computers move the computer randomly put symbol into the table
       point = randrange(count)
       row,col = free[point]
       board[row][col] = 'X'

