from piece import *
from colour import *
import os

def numify(text):
    return str(ord(text.upper()) - 65)

def alphify(num):
    return chr(num + 97)

def boldify(text):
    return (colour.BOLD + text + colour.END)

def redify(text):
    return (colour.RED + boldify(text) + colour.END)

def selected(text):
    return (colour.GREEN + boldify(text) + colour.END)

def board_init():
    board = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        for k in range(8):
            board[i].append(Piece(None, "e", "."))
    
    return board

def board_print(board, selected_col=None, selected_row=None, movementBoard=None):
    os.system("clear")

    temp = "temporary print"

    if selected_col and selected_row:
        colly = numify(selected_col)

        print("SELECTED " + colly + "," + str(selected_row))
        selected_col = int(colly)
        selected_row = int(selected_row)
    else:
        print("NOTHING SELECTED")
        selected_col = -1
        selected_row = -1

    print("   ________________________")
    for row in range(8):
        print(row, end="")
        print(" |", end="")
        for col in range(8):
            if(row == selected_row and col == selected_col):
                print(selected(board[row][col].toString()) + " |", end="")
                temp = moveset(board, selected_col, selected_row)
            else:
                print(board[row][col].toString() + " |", end="")
        print("\n", end="")
    
    print("   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("   a  b  c  d  e  f  g  h\n")

    print(temp)

def board_setup(board):    
    for i in range(8):
        board[1][i] = Piece("black", "P", "♟︎")
    
    board[0][0] = board[0][7] = Piece("black", "R", "♜")
    board[0][1] = board[0][6] = Piece("black", "K", "♞")
    board[0][2] = board[0][5] = Piece("black", "B", "♝")
    board[0][3] = Piece("black", "Q", "♛")
    board[0][4] = Piece("black", "G", "♚")

    for i in range(8):
        board[6][i] = Piece("white", "p", "♙")
    
    board[7][0] = board[7][7] = Piece("white", "r", "♖")
    board[7][1] = board[7][6] = Piece("white", "k", "♘")
    board[7][2] = board[7][5] = Piece("white", "b", "♗")
    board[7][3] = Piece("white", "q", "♕")
    board[7][4] = Piece("white", "g", "♔")

def moveset(board, selected_col, selected_row):
    dummyBoard = board_init()

    piece = board[selected_row][selected_col]

    typ = piece.type.upper()

    if(typ == "P"):
        return("pawn at " + str(alphify(selected_col)) + str(selected_row))
    elif(typ == "R"):
        return("rook at " + str(alphify(selected_col)) + str(selected_row))
    elif(typ == "K"):
        return("knight at " + str(alphify(selected_col)) + str(selected_row))
    elif(typ == "B"):
        outline_diagonal(board, 5, 3)
        return("bishop at " + str(alphify(selected_col)) + str(selected_row))
    elif(typ == "Q"):
        return("queen at " + str(alphify(selected_col)) + str(selected_row))
    elif(typ == "G"):
        return("king at " + str(alphify(selected_col)) + str(selected_row))
    
    return "empy space"

def outline_diagonal(board, col, row):
    x = col
    y = row

    i = 1

    moveX = next_diag(x, y, i, i)[1]
    moveY = next_diag(x, y, i, i)[0]

    dummyBoard = board_init()

def ooutline_diagonal(board, col, row):
    dummyBoard = board

    x = col
    y = row

    i = 1
    #while (i < 8):

    moveX = next_diag(x, y, i, i)[1]
    moveY = next_diag(x, y, i, i)[0]
    while(dummyBoard[moveX][moveY].team != None) and (i < 8):
        dummyBoard[moveX][moveY] = Piece("x", redify("x"))
        moveX= next_diag(x, y, i, i)[1]
        moveY = next_diag(x, y, i, i)[0]
        print(i)
        i += 1
        #dummyBoard[next_diag(x, y, i, -i)[1]][next_diag(x, y, i, -i)[0]] = Piece("x", redify("x"))
        ##dummyBoard[next_diag(x, y, -i, i)[1]][next_diag(x, y, -i, i)[0]] = Piece("x", redify("x"))
        dummyBoard[next_diag(x, y, -i, -i)[1]][next_diag(x, y, -i, -i)[0]] = Piece("x", redify("x"))
        #i += 1

    print("SATRT")
    board_print(dummyBoard)
    print("END")
    return dummyBoard

def next_diag(x, y, xOffset, yOffset):
    retX = x + xOffset
    retY = y + yOffset

    if (0 > retY) or (7 < retY) or (0 > retX) or (7 < retX):
        return [x, y]
    
    return ([x + xOffset, y + yOffset])

def outline_lateral(board, col, row):
    return