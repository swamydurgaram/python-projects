#from IPython.display import clear_output

#function that can print out a board.
def display_board(board):
    #clear_output()  # Remember, this only works in jupyter!
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

#function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# take position assigns marker it to the board
def place_marker(board, marker, position):
    board[position] = marker
    
# chech win or not
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
 
import random
# randomly change the first player
def choose_first():
    if random.randint(0,1)==0:
        return 'player 2'
    else:
        return 'player 1'

#check is there any spaces or not
def space_check(board, position):
    
    return board[position]==' '

# to check the board is full or not
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
# to take player choice to marker on board from 1 to 9
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
# ask players to play again or not
def replay():
         
    return input('Are you ready to play? Enter Yes or No.').lower().startswith('y')
 
#hard part of program and creating player 1, player 2 play
print('Welcome to Tic Tac Toe!')

while True:
    #while True:
    test_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    
    # Set the game up here
    #pass
    while game_on: #while game_on:
        if turn=='player 1':  #Player 1 Turn
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player1_marker,position)
            
            if win_check(test_board,player1_marker):
                display_board(test_board)
                print('PLAYER 1 HAS WON !!')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('THE GAME IS A DRAW !!')
                    break
                else:
                    turn = 'player 2'
            
        
        
        else: # Player2's turn.
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player2_marker,position)
            
            if win_check(test_board,player2_marker):
                display_board(test_board)
                print('PLAYER 2 HAS WON !!')
                game_on = False
            else:
                if full_board_check(test_board):
                    display_board(test_board)
                    print('THE GAME IS A DRAW !!')
                    break
                else:
                    turn = 'player 1'
            
            

    if not replay(): #if not replay():
        break
        #break
        
