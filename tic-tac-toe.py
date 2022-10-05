from telnetlib import STATUS

import random as rd

# the robot
def Robot(board):
    n= rd.randint(1,9)
    while board[n] != ' ':
        n = rd.randint(1, 9)
    return int(n)
    #we have to check the board array too in the process

# Printing the Board on the Screen
def printfield(board):
    print("                    ",board[1],"|",board[2],"|",board[3])
    print("                     - + - + -")
    print("                    ",board[4],"|",board[5],"|",board[6])
    print("                     - + - + -")
    print("                    ",board[7],"|",board[8],"|",board[9])

# Placing a Mark on the Board
def makeMove(board, letter, move):
    board[move] = letter
    
# Checking Whether a Space on the Board Is Free
def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ' '

# Checking Whether the Player Won
def Iswinner(board, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
    return (le == board[1] and le == board[2] and le == board[3]) or (le == board[4] and le == board[5] and le == board[6]) or (le == board[7] and le == board[8] and le == board[9]) or (le == board[1] and le == board[5] and le == board[9]) or (le == board[3] and le == board[5] and le == board[7]) or (le == board[1] and le == board[4] and le == board[7]) or (le == board[2] and le == board[5] and le == board[8]) or (le==board[3] and le== board[6] and le== board[9])

# Deciding Who Goes First
def whoGoesFirst():
     # Randomly choose which player goes first.
    if rd.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

# Letting the Player Choose X or O
def inputPlayerLetter():
    # Lets the player enter which letter they want to be.
    # Returns a list with the player's letter as the first item and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


# Choosing a Move from a List of Moves
def chooseRandomMoveFromList(board, movesList):
     # Returns a valid move from the passed list on the passed board.
     # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
#checking if the board is full
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

# the actual game

while True:
    board = [' '] * 10
    name = input("write your name: ")
    print("Welcome ", name, " to Tic-Tac-Toe!")
    print('''
      Note: the game is gonna look just like that:
      
                    1|2|3
                    -+-+-
                    4|5|6
                    -+-+-
                    7|8|9
                    
      ''')
    choice = whoGoesFirst()
    playerLetter, computerLetter = inputPlayerLetter()    
    win = True
    print('The ' + choice + ' will go first.')
    game = True
    while game:
        printfield(board)
        if choice == 'player':
            # Player's turn
            printfield(board)
            
            move = int(input('What is your next move? (1-9) '))
            while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('please write a number between 1->9') #there is a bug here
                move=int(input())
            while not isSpaceFree(board, move):
                # there is a bug here
                print('the move has already been taken, please use an other move')
                move=int(input())

            makeMove(board, playerLetter, move)
            if Iswinner(board, playerLetter):
                printfield(board)
                print('Hooray! You have won the game!')
                game = False
            else:
                if isBoardFull(board):
                    printfield(board)
                    print('the game is a tie')
                    break
                else:
                    choice = 'computer'

        else:
            # Computer's turn
            move = Robot(board)
            makeMove(board, computerLetter, move)
            
            if Iswinner(board, computerLetter):
                printfield(board)
                print('The computer has won the game!')
                game = False
            else:
                if isBoardFull(board):
                    printfield(board)
                    print('the game is a tie')
                    break
                else:
                    choice = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
