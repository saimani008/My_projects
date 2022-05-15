def EnterMove(board):
    temp = False
    while(not temp):       # this function asks the user to enter the number at where we want to put the symbol
         move = input("Enter your move: ")    #checks if the entered number is valid or not
         temp = (len(move)==1) and move>='1' and move<='9'
         if(not temp):
            print("invalid move try again")
            continue
         move = int(move)-1
         row  = move//3
         col  = move%3
         sign = board[row][col]
         temp = sign  not in ['O','X']
         if(not temp):
           print("already occupied enter another one")
           continue
    board[row][col] = 'O'
