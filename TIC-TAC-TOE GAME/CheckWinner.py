def check(board,sign):
    if(sign=='X'):
       who = 'me'
    elif(sign=='O'):
       who = 'you'
    else:
       who = None                #this function checks who won the game
    diagonal1= diagonal2 = True
    for i in range(3):
        if(board[i][0]==sign and board[i][1]==sign and board[i][2]==sign):
            return who
        if(board[0][i]==sign and board[1][i]==sign and board[2][i]==sign):
            return who
        if(board[i][i]!=sign):
           diagonal1 = False
        if(board[2-i][2-i]!=sign):
           diagonal2 = False
    if(diagonal1 or diagonal2):
        return who
    return None
