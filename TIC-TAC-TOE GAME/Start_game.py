from random import randrange
from display import display_board
from Enter_move import EnterMove
from List_of_free_fields import listOfFreeFields
from Computer_move import computerMove
from check_winner import check

board = [[3*j+i+1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
free = listOfFreeFields(board)   # it returns all the available free places in the table .
human_turn = True
while(len(free)):
    display_board(board)
    if(human_turn):        
       EnterMove(board)
       win = check(board,'O')
    else:
       computerMove(board)
       win = check(board,'X')
    if(win!=None):
        break
    human_turn = not human_turn
    free = listOfFreeFields(board)



display_board(board)       # the table is dipalyed 
if(win=='you'):
   print("You Won!")
elif(win=='me'):
  print("I Won!")
else:
  print("Tie!")
