import sys
import os

from boardFunctions import *
from piece import *
from stateCycles import *

os.system("clear")

board = board_init()

board_setup(board)
board_print(board)


if(menu()):
    os.system("clear")
    board_print(board)
    print("\nThanks for not playing!")
    sys.exit(0)

inp = "aa"
col = None
row = None

while(not mate(board, inp)): #while there's no checkmate
    board_print(board, col, row)
    inp = pieceSelection(board) #get the user's next piece selection

    col = inp[0]
    row = inp[1]

    print("HELLO")