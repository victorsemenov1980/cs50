"""
Tic Tac Toe Player
"""

import math
from math import inf as infinity

import copy
import random
moves=set()

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
    qX=0
    qO=0
    for i in board:
        qX+=i.count(X)
        qO+=i.count(O)
    if qX==qO:
        return X
    elif qX>qO:
        return O
        
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action=[]
    actions=set()
    # print(board)
    for i in range(len(board)):
        # print('I',i)
        for j in range(len(board[i])):
            if board[i][j]==None:
                action.append(i)
                action.append(j)
                
                x=tuple(action)
                actions.add(x)
                # print(actions)
                action=[]
                x=()
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    res_board=copy.deepcopy(board)
    try:
        action in actions(board)
        res_board[action[0]][action[1]]=player(board)
    except:
        return 'action is not valid'
    return res_board
    

def count_values(iterable):
     
    if iterable.count(iterable[0])==len(iterable):
        return True
    else:
        return False
    
    
def win_routes():
    return [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],
            [(2,0),(2,1),(2,2)],[(0,0),(1,0),(2,1)],[(0,1),
            (1,1),(2,1)],[(0,2),(1,2),(2,2)],[(0,0),(1,1),
            (2,2)],[(0,2),(1,1),(2,0)]]


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_list=[]
    check=[]
    win_list.append([board[0][0],board[0][1],board[0][2]])
    win_list.append([board[1][0],board[1][1],board[1][2]])
    win_list.append([board[2][0],board[2][1],board[2][2]])
    win_list.append([board[0][0],board[1][0],board[2][0]])
    win_list.append([board[0][1],board[1][1],board[2][1]])
    win_list.append([board[0][2],board[1][2],board[2][2]])
    win_list.append([board[0][0],board[1][1],board[2][2]])
    win_list.append([board[0][2],board[1][1],board[2][0]])
    for i in win_list:
        if count_values(i)==True and i[0]!=None:
            check.append(i)
    if len(check)>0: 
        if len(check)!=1:
            return 'impossible board'
        if check[0][0]==X:
            return X
        elif check[0][0]==O:
            return O
    else:
            return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board))==0 or winner(board)!=None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    center=(1,1)
    corners=[(0,0),(0,2),(2,0),(2,2)]
    if terminal(board)==True:
        return None
    else:
        if player(board)==X and board==initial_state():
            print('Player X, board Initial')
            i=random.randint(0, 3)
            move=corners.pop(i)
            print('Move=',move)
            return move
        elif player(board)==O and len(actions(board))==8 and center in actions(board):
            print('Player 0,move2',center)
            return center
        elif player(board)==X and len(actions(board))==7 and center not in actions(board):
            i=random.randint(0, 2)
            print('Player X, move 3',corners[i])
            return corners[i]
        else:
            current_player = player(board)

        if current_player == X:
            v = -math.inf
            for action in actions(board):
                print(action)
                k = min_value(result(board, action))  
                print('K-X=',k)
                if k > v:
                    v = k
                    best_move = action
        else:
            v = math.inf
            for action in actions(board):
                print(action)
                k = max_value(result(board, action))  
                print('K-O=',k)
                if k < v:
                    v = k
                    best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    # print(v)
    return v    

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v    
        
        
board=[[X, EMPTY, EMPTY],
            [EMPTY, O, EMPTY],
            [X, EMPTY, EMPTY]]

print(minimax(board))    

'''
function minimax(board, depth, isMaximizingPlayer):

    if current board state is a terminal state :
        return value of the board
    
    if isMaximizingPlayer :
        bestVal = -INFINITY 
        for each move in board :
            value = minimax(board, depth+1, false)
            bestVal = max( bestVal, value) 
        return bestVal

    else :
        bestVal = +INFINITY 
        for each move in board :
            value = minimax(board, depth+1, true)
            bestVal = min( bestVal, value) 
        return bestVal


function findBestMove(board):
    bestMove = NULL
    for each move in board :
        if current move is better than bestMove
            bestMove = current move
    return bestMove
        
'''
            