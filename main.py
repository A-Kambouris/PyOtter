
#board representation, think of it as starting from bottom left, (1,a) array will be 12x12

#colour list 1 is white, -1 is black, 0 is empty,99 is out of bounds


startingColourList =\
    [99,99,99,99,99,99,99,99,99,99,99,99,
     99,99,99,99,99,99,99,99,99,99,99,99,
     99,99,1,1,1,1,1,1,1,1,99,99,
     99,99,1,1,1,1,1,1,1,1,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,-1,-1,-1,-1,-1,-1,-1,-1,99,99,
     99,99,-1,-1,-1,-1,-1,-1,-1,-1,99,99,
     99,99,99,99,99,99,99,99,99,99,99,99,
     99,99,99,99,99,99,99,99,99,99,99,99]

#piece list 1 is pawn, 2 is knight, 3 is bishop, 4 is rook, 5 is queen, 6 is king, 0 is empty
startingPieceList =\
    [99,99,99,99,99,99,99,99,99,99,99,99,
     99,99,99,99,99,99,99,99,99,99,99,99,
     99,99,4,2,3,5,6,3,2,4,99,99,
     99,99,1,1,1,1,1,1,1,1,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,0,0,0,0,0,0,0,0,99,99,
     99,99,1,1,1,1,1,1,1,1,99,99,
     99,99,4,2,3,5,6,3,2,4,99,99,
     99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99,
     99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]

startingBoard = [startingColourList, startingPieceList]
print(len(startingColourList))
print(len(startingPieceList))

currentBoard = startingBoard

#move representation, create a list of possible moves

def pawn_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []
    #these two are for single pawn moves and check if the space is empty

    match col:
        case 1:
            if currentBoard[0][position+12] == 0:
                possibleMoves.append(position+12) #this  are for single pawn moves and check if the space is empty
            if currentBoard[0][position + 24] == 0 and currentBoard[0][position + 12] == 0 and (38 <= position <= 45):
                possibleMoves.append(position + 24) #this check of the pawn is on its starting space and does the empty space checks for the double pawn move
            if currentBoard[0][position+11] == -1:
                possibleMoves.append(position+11)
            if currentBoard[0][position+13] == -1:
                possibleMoves.append(position+13)
        case -1:
            if currentBoard[0][position-12] == 0:
                possibleMoves.append(position-12)
            if currentBoard[0][position - 24] == 0 and currentBoard[0][position - 12] == 0 and (98 <= position <= 105):
                possibleMoves.append(position - 24)
            if currentBoard[0][position - 11] == 1:
                possibleMoves.append(position - 11)
            if currentBoard[0][position - 13] == 1:
                possibleMoves.append(position - 13)

    return [possibleMoves]

def king_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []

    # this can definitely be rewritten but do it later, it seems to work

    if currentBoard[0][position+12] == 0:
        possibleMoves.append(position+12)

    if currentBoard[0][position+11] == 0:
        possibleMoves.append(position+11)

    if currentBoard[0][position+13] == 0:
        possibleMoves.append(position+13)

    if currentBoard[0][position-12] == 0:
        possibleMoves.append(position-12)

    if currentBoard[0][position-11] == 0:
        possibleMoves.append(position-11)

    if currentBoard[0][position-13] == 0:
        possibleMoves.append(position-13)


    if currentBoard[0][position-1] == 0:
        possibleMoves.append(position-1)

    if currentBoard[0][position+1] == 0:
        possibleMoves.append(position+1)

def rook_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []

    for x in range(1,8):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == 99:
            break

    for x in range(1,8):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)
        if currentBoard[0][position-x] == 99:
            break

    for x in range(12,96,12):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == 99:
            break

    for x in range(12,96,12):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)
        if currentBoard[0][position-x] == 99:
            break

def bishop_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []

    for x in range(13,200,13):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == 99:
            break

    for x in range(13,200,13):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)
        if currentBoard[0][position-x] == 99:
            break

    for x in range(11,200,11):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == 99:
            break

    for x in range(11,200,11):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)
        if currentBoard[0][position-x] == 99:
            break

def knight_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []


i = 0
while i<144:

    match currentBoard[1][i]:

        case 1:
            print("Pawn moves:")
            print(pawn_moves(currentBoard, i))
        case 6:
            print("King moves:")
            print(king_moves(currentBoard, i))
        case 4:
            print("Rook moves:")
            print(rook_moves(currentBoard, i))
        case 3:
            print("Bishop moves:")
            print(bishop_moves(currentBoard, i))

    i+=1