"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # In the initial game state, X gets the first move.
    if board == initial_state():
        return X

    # The player who has the next turn on a board is the one with the less moves on the board
    else:
        totalmoves_playerX = 0
        totalmoves_playerO = 0

        # Iterate over the two-dimensional array (board) and keep track of the number of moves played by X and O
        for row in board:
            totalmoves_playerX += row.count(X)
            totalmoves_playerO += row.count(O)

        # As the player alternates with each additional move
        # If the total number of moves for player X exceeds that of player O, player X is one move ahead than player X and it is thus O's turn and vice versa
        if totalmoves_playerO < totalmoves_playerX:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i corresponds to the row of the move (0, 1, or 2)
    j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    """

    possible_moves = set()

    # Iterate over each cell on the board. Possible moves are any cells on the board that do not already have an X or an O in them.
    for i in range(3):
        for j in range(3):
            
            if board[i][j] == EMPTY:
                move = (i, j)
                possible_moves.add(move)
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move / action (i, j) on the board.
    """
    valid_actions = actions(board)

    if action in valid_actions == False:
        raise ValueError('action is not a valid action for the board.')
    else: 

        # Store the i,j coordinates of the action in distinct variables that will be used to update the deep copy of the board with the user's move
        i = action[0] 
        j = action[1] 

        #  Make a deep copy of the board; the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation.
        duplicate_board = deepcopy(board)

        # Determine who's turn it is in order to determine which letter to put on the deepcopy of the board
        next_player = player(board) 
        current_player = ''

        if next_player == O:
            current_player = 'X'
        if next_player == X:
            current_player = 'O'

        # Populate the cell located at the coordinates for the player's move (action) in the deep copy of the board with current_player (X or O).
        #duplicate_board[i][j] = current_player
        duplicate_board[i][j] = next_player

        return duplicate_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    """

    totalmoves_playerX = 0
    totalmoves_playerO = 0

    # ROWS: check if 3 "xxx" or 3 "ooo"
    for row in board:
        totalmoves_playerX += row.count("X")
        print(totalmoves_playerX)
        totalmoves_playerO += row.count("O")
        print(totalmoves_playerO)

        if totalmoves_playerX == 3:
            return X
        if totalmoves_playerO == 3:
            return O

    # Traverse the board. Extract the values at the different coordinates and store them as strings inside column or diagonal and check for patterns to determine who is the winner

    # COLUMNS
    # X or O
    # X    O
    # X    O

    for j in range(3):
        column = ''
        for i in range(3):
            column += str(board[i][j])

        if column == 'XXX':
            return X
        if column == 'OOO':
            return O

    # DIAGONALS
    # diagonal_1 
    # X    or O
    #  X       O
    #   X       O
    # diagonal 2
    #   X or   O
    #  X      O
    # X      O
    
    diagonal_1 = ''
    j_diagonal1 = 0
    
    diagonal_2 = ''
    j_diagonal2 = 2

    for i in range(3):
        diagonal_1 += str(board[i][j_diagonal1])
        j_diagonal1 += 1

        diagonal_2 += str(board[i][j_diagonal2])
        j_diagonal2 -= 1

    if diagonal_1 == 'XXX' or diagonal_2 == 'XXX':
        return X
    if diagonal_1 == 'OOO' or diagonal_2 == 'OOO':
        return O
    
    # If there is no winner of the game (either because the game is in progress, or because it ended in a tie), return None
    else:
        return None





def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Return true if the game is over because someone has won the game. Another way of implementing this that is more higher level would have been to check if winner(board) is not None.
    if (winner(board) == X) or (winner(board) == O):
        return True
    
    # Traverse the board and count the number of EMPTY cells. Return true if the game is over because all cells have been filled without anyone winning (there are no more EMPTY cells on the game). Return False if the game is still in progress (there are still EMPTY cells on the board).
    # Another way to implement this would have been to check if actions(board) is not None (meaning that the game is still in progress as there are possible moves left)
    total_emptycells = 0
    for row in board:
        total_emptycells += row.count(EMPTY)

    if total_emptycells == 0:
        return True

    else:
        return False

        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if (game_winner == X):
        return 1
    if (game_winner == O):
        return -1
    if (not game_winner):
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    An optimal action (i, j) is an action that maximizes the utility for the current player.
    The optimal action must be an allowable action on the board. If multiple moves are equally optimal, any of these moves is acceptable.
    """
    if terminal(board):
        return None
    
    # Create a set of valid_actions for the current board
    valid_actions = actions(board)

    # Determine who the current player is
    next_player = player(board) 
    current_player = ''

    if next_player == O:
        current_player = 'X'
    if next_player == X:
        current_player = 'O'

    # The maximizing player (current player) picks action a in valid_actions that produces the highest value of Min-value(Result(board, a))
    if current_player == O:
        possiblemoveresults = []
        for action in valid_actions:
            possiblemoveresults.append([minValue(result(board, action)), action])
        return sorted(possiblemoveresults, key=lambda x: x[0], reverse=True)[0][1]

    elif current_player == X:
        possiblemoveresults = []
        for action in valid_actions:
            possiblemoveresults.append([maxValue(result(board, action)), action])
        return sorted(possiblemoveresults, key=lambda x: x[0])[0][1]

    # Given board
    
    for action in valid_actions:
        maxValue(board)

    # The minimizing player (nex_player) picks action a in valid_actions that produces the lowest value of Max-value(Result(board,a))

def maxValue(board):
    v = float('-inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,minValue(result(board, action)))
    return v
    

def minValue(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v,maxValue(result(board, action)))
    return v
