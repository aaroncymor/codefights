"""
You are given an n x n chessboard, stored in a two-dimensional array. There are some white and black chess pieces on it.

A normal chess rook of the given color is placed on the cell 'square'. The square is given in the standard chess notation, e.g. "a1", "h3", "b2". The position "a1" is in the lower left corner; "b1" is the square to the right-hand side of "a1"; "a2" is the square above "a1."

Your task is to return all possible moves the rook can take, sorted by squares' letters and numbers.

Example

For

chessboard = [[1, 1, 1, 0],
              [1, -1, 1, 1],
              [1, 0, 0, 0],
              [0, 0, 0, 1]],
square = "b1",
color = 1

the output should be
PossibleRookMoves(chessboard, square, color) = ["a1", "b2", "b3", "c1"].

square = "b1" means that it is to be placed at chessboard[3][1], so the rook can move to the following squares:

    "a1", since it is empty (it's impossible to move further in this direction since that's the end of the chessboard);
    "b2", since it is empty;
    "b3", since it is occupied by the opponent's piece (note, however, that it is not possible to move further in this direction);
    "c1", since it is empty (however, the rook cannot move further since the next piece is the piece of the same color).

Sorting these positions in ascending order by letter and by number, the result therefore is ["a1", "b2", "b3", "c1"].

    [input] array.array.integer chessboard
        A two-dimensional array that represents a square chessboard. A value of 1 indicates that the corresponding position is occupied by a white piece; a value of 0 indicates that it is empty; a value of -1 indicates that it is occupied by a black piece. It is guaranteed that the chessboard is not greater than 8 x 8 in size.

    [input] string square
        The square the rook is placed on. It is guaranteed that it belongs to the chessboard and is not occupied.

    [input] integer color
        The color of the rook piece (1 for white, -1 for black).

    [output] array.string
        All possible moves the rook can make sorted as described above
"""
results = []
def moveUp(chessboard,ri,ci,oci,color):
    if ci >= 0:
        if(chessboard[ci][ri] + chessboard[oci][ri]) == 0:
            results.append((ci,ri))
        elif (chessboard[ci][ri] + chessboard[oci][ri]) == color:
            results.append((ci,ri))
            moveUp(chessboard,ri,ci-1,oci,color)

def moveDown(chessboard,ri,ci,oci,color):
    if ci < len(chessboard):
        if(chessboard[ci][ri] + chessboard[oci][ri]) == 0:
            results.append((ci,ri))
        elif (chessboard[ci][ri] + chessboard[oci][ri]) == color:
            results.append((ci,ri))
            moveDown(chessboard,ri,ci+1,oci,color)

def moveLeft(chessboard,ri,ci,ori,color):
    if ri >= 0:
        if(chessboard[ci][ri] + chessboard[ci][ori]) == 0:
            results.append((ci,ri))
        elif (chessboard[ci][ri] + chessboard[ci][ori]) == color:
            results.append((ci,ri))
            moveLeft(chessboard,ri-1,ci,ori,color)

def moveRight(chessboard,ri,ci,ori,color):
    if ri < len(chessboard[0]):
        if(chessboard[ci][ri] + chessboard[ci][ori]) == 0:
            results.append((ci,ri))
        elif (chessboard[ci][ri] + chessboard[ci][ori]) == color:
            results.append((ci,ri))
            moveRight(chessboard,ri+1,ci,ori,color)


def PossibleRookMoves(chessboard,square,color):
    cols,rows = len(chessboard),len(chessboard[0])
    letters = ['a','b','c','d','e','f','g','h']

    row_index = letters.index(square[0])
    col_index = cols - int(square[1])

    if row_index < rows and col_index >= 0 and col_index < cols:
        chessboard[col_index][row_index] = color
        moveUp(chessboard,row_index,col_index - 1,col_index,color)
        moveDown(chessboard,row_index,col_index + 1,col_index,color)
        moveLeft(chessboard,row_index - 1,col_index,row_index,color)
        moveRight(chessboard,row_index + 1,col_index,row_index,color)
        
    return sorted([letters[r] + str(cols - c) for c, r in results])

chessboard = [
             [0,0,1,0], 
             [1,1,0,1], 
             [0,0,1,0], 
             [0,0,1,0]]
square = "c3"
color = -1

print PossibleRookMoves(chessboard,square,color)
