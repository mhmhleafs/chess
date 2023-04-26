import os

from boardFunctions import *
from winCheck import *
import constants

def menu():
    print("Welcome to chess!")
    print("Menu:")
    print("\t(s) : start")
    print("\t(x) : exit")
    print("\ncommand:")
    inp = input()
    while(inp != "x" and inp != "s"):
        print("\nInvalid input length")
        print("command:")
        inp = input()

    return inp=="x"
    

def pieceSelection(board, error_message=""):

    print("\n" + error_message)
    print("Select a piece (or type xx to forfeit): ", end="")
    inp = input()
    

    if(len(inp) != 2):
        board_print(board)
        inp = pieceSelection(board, "Invalid input length")

    if(inp[0] not in constants.COLS and inp != "xx"):
        board_print(board)
        inp = pieceSelection(board, "Invalid column selected")

    if(inp[1] not in constants.ROWS and inp != "xx"):
        board_print(board)
        inp = pieceSelection(board, "Invalid row selected")


    return inp