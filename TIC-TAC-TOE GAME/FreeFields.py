def listOfFreeFields(board):
    free = []
    for row in range(3):
        for col in range(3):
             if(board[row][col] not in ['O','X']):
                  free.append((row,col))
    return free

