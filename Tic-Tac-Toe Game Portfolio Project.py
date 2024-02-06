# Portfolio Project 1 - Terminal Game
import random

def draw_board(board):
    # This function prints out the game board.
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    # Lets the player choose which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter - input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def who_goes_first():
    # Randomly selects which player goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    
def play_again():
    # Function returns True if the player wants to play again, otherwise it returns False.
    print('Would you like to play again? (Yes or No)')
    return input().upper().startswith('Y')

def make_move(board, letter, move):
    board[move] = letter

def has_won(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board_copy(board):
    # Makes a duplicate of the board list and returns the duplicate.
    copy_board = []
    for i in board:
        copy_board.append(i)
    return copy_board

def is_space_free(board, move):
    # Return True if the passed move is free on the passed game board.
    return board[move] == ' '

def get_player_move(board):
    # Let's the player make their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def choose_random_move_from_list(board, moves_list):
    # Returns a valid move from the passed list on the passed game board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None
    
def get_ai_move(board, ai_letter):
    # Given a board and the AI's letter, determine where to move and return that move.
    if ai_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Algorithm for the Tic-Tac-Toe AI.
    # Checks to see if the AI can win in the next move.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, ai_letter, i)
            if has_won(copy, ai_letter):
                return i
            
    # Checks if the player could win in the next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if has_won(copy, player_letter):
                return i
            
    # Try to take one of the croners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5
    
    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise returns False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True

print("Michael's Tic-Tac-Toe Game!")

while True:
    # Reset the game board.
    game_board = [' '] * 10
    player_letter, ai_letter = input_player_letter()
    turn = who_goes_first()
    print('The '+ turn + ' will go first.')
    game_is_active = True

    while game_is_active:
        if turn == 'player':
            # Player's turn.
            draw_board(game_board)
            move = get_player_move(game_board)
            make_move(game_board, player_letter, move)

            if has_won(game_board, player_letter):
                draw_board(game_board)
                print('Congratulations! You won the game!')
                game_is_active = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print('The game ends in a draw.')
                    break
                else:
                    turn = 'computer'

        else:
            # The AI's turn.
            move = get_ai_move(game_board, ai_letter)
            make_move(game_board, ai_letter)
            if has_won(game_board, ai_letter):
                draw_board(game_board)
                print('The computer has defeated you. You lose.')
                game_is_active = False
            else:
                if is_board_full(game_board):
                    draw_board(game_board)
                    print('The game ends in a draw')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break