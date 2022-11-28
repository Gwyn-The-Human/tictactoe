"""
Tic Tac Toe Player
"""

import math
import copy
from pickle import NONE


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
    Xcounter = 0
    Ocounter = 0
    for row in board:
        for cell in row:
            if cell == X:
                Xcounter+=1
            if cell == O: 
                Ocounter +=1
    if Xcounter == Ocounter:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    Actions = set()
    RowCount = 0
    for row in board:
        CellCount = 0
        for cell in row:
            if cell == EMPTY:
                x = (RowCount, CellCount)
                Actions.add (x)
            CellCount += 1
        RowCount+=1
    return Actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    class InvalidMove (Exception):
        pass
    try:
        Turn = player(board) 
        NewBoard = copy.deepcopy (board) 
        if NewBoard [action[0]] [action[1]] == EMPTY:
            NewBoard [action[0]] [action[1]] = Turn # fills in the space designated by the action with the symbol of whose turn it is.
            return NewBoard 
        else: 
            raise InvalidMove
    except (InvalidMove):
        print ("Invalid Move! Choose an empy space!") 
        

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range (0,3): #for column, if each space in the colomn is the same; check one space and return whats in it
        if board [i][0] == board [i][1] == board [i][2] and board [i][0] != EMPTY:
            return board [i][0]
            
    for j in range (0,3): #same as above, with rows
        if board [0][j] == board [1][j] == board [2][j] and board [0][j] != EMPTY:
            return board[0][j]
  
    if board [0][0] == board [1][1] == board [2][2] or board [2][0]== board[1][1] == board [0][2]:#diagonals
        if board [1][1] != EMPTY:

            return board[1][1] #return the value in the middle space if it is not empty

    return None #if there is a winner, it should return a value before it gets to this point. 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner (board) == None: #if no winner
        for row in board:
            for cell in row:
                if cell == EMPTY:#if there is a single space
                    return False #game continues
    return True #if there is no space, or there is space BUT there is also a winner; reverts to True (Game Over)
            

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    Victor = winner (board)
    if Victor == X:
        return 1
    if Victor == O:
        return -1
    else:
        return 0
    

def minimax(board):

    """
    Returns the optimal action for the CURRENT player on the board. "If the board is a terminal board, the minimax function should return None".
    """
    if terminal (board): 
        return None
    elif player (board) == X:  # if its x's turn, then 
        OptimalMove = NONE
        Highest = -math.inf
        for move in actions (board):
            val = ValMin (result (board,move))
            #print (str (move) + " move has a value of " + str (val) + ". current highest is" + str (Highest))
            if val >= Highest:
               OptimalMove = move
               Highest = val
               #print ("Max players best move is " + str(OptimalMove))
        return OptimalMove
    elif player (board) == O: 
        OptimalMove = NONE
        Lowest = math.inf
        for move in actions (board):
            val = ValMax (result (board,move))
            if val <= Lowest: 
               OptimalMove = move
               Lowest = val
        return OptimalMove


def ValMax (board): 
    if terminal(board):
        return utility(board)
    MaxTuple = -math.inf
    for move in actions(board):
        MinTuple = ValMin(result (board, move)) 
        if MaxTuple <= MinTuple:
            MaxTuple = MinTuple 
    return MaxTuple


def ValMin (board): 
    if terminal(board):
        return utility(board)
    MinTuple = math.inf         
    for move in actions(board):
        MaxTuple = ValMax(result (board, move))
        if MinTuple  >= MaxTuple: 
            MinTuple = MaxTuple
    return MinTuple






