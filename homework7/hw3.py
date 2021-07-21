"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """The function checks the tic_tac_toe board and returns game result
    if it's finished, unfinished otherwise"""
    b_size = len(board)
    if '-' in [row[column] for row in board for column in range(b_size)]:
        return "unfinished!"
    else:
        for i in [[x[i] for x in board] for i in range(b_size)]:
            if len(set(i)) == 1:
                return f'{i[0]} wins!'
        for i in [x for x in board]:
            if len(set(i)) == 1:
                return f'{i[0]} wins!'
        for i in ([board[i][-i-1] for i in range(b_size)],
                  [board[i][i] for i in range(b_size)]):
            if len(set(i)) == 1:
                return f'{i[0]} wins!'
            else:
                return 'draw!'
