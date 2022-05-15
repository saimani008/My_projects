def display_board(board):      #this function displays the board
    print("+-------"*3+"+")    #it takes the parameter board and display the game board
    for row in range(3):
        print("|       "*3+"|")
        for col in range(3):
            print("|   "+str(board[row][col])+"   ",end="")
        print("|")
        print("|       "*3+"|")
        print("+-------"*3+"+")
