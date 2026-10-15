from operator import truediv

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

    return possibleMoves

def king_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []



    # this can definitely be rewritten but do it later, it seems to work

    if currentBoard[0][position+12] == 0 or currentBoard[0][position+12] == -col:
        possibleMoves.append(position+12)

    if currentBoard[0][position+11] == 0 or currentBoard[0][position+11] == -col:
        possibleMoves.append(position+11)

    if currentBoard[0][position+13] == 0 or currentBoard[0][position+13] == -col:
        possibleMoves.append(position+13)

    if currentBoard[0][position-12] == 0 or currentBoard[0][position-12] == -col:
        possibleMoves.append(position-12)

    if currentBoard[0][position-11] == 0 or currentBoard[0][position-11] == -col:
        possibleMoves.append(position-11)

    if currentBoard[0][position-13] == 0 or currentBoard[0][position-13] == -col:
        possibleMoves.append(position-13)


    if currentBoard[0][position-1] == 0 or currentBoard[0][position-1] == -col:
        possibleMoves.append(position-1)

    if currentBoard[0][position+1] == 0 or currentBoard[0][position+1] == -col:
        possibleMoves.append(position+1)

    return possibleMoves


def rook_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []

    for x in range(1,8):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == -col:
            possibleMoves.append(position+x)
            break
        if currentBoard[0][position+x] == 99 or currentBoard[0][position+x] == col:
            break

    for x in range(1,8):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)

        if currentBoard[0][position-x] == -col:
            possibleMoves.append(position-x)
            break
        if currentBoard[0][position-x] == 99 or currentBoard[0][position-x] == col:
            break

    for x in range(12,96,12):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == -col:
            possibleMoves.append(position+x)
            break
        if currentBoard[0][position+x] == 99 or currentBoard[0][position+x] == col:
            break

    for x in range(12,96,12):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)
        if currentBoard[0][position-x] == -col:
            possibleMoves.append(position-x)
            break
        if currentBoard[0][position-x] == 99 or currentBoard[0][position-x] == col:
            break

    return possibleMoves

def bishop_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []

    for x in range(13,200,13):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == -col:
            possibleMoves.append(position+x)
            break
        if currentBoard[0][position+x] == 99 or currentBoard[0][position+x] == col:
            break

    for x in range(13,200,13):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)
        if currentBoard[0][position-x] == -col:
            possibleMoves.append(position-x)
            break
        if currentBoard[0][position-x] == 99 or currentBoard[0][position-x] == col:
            break

    for x in range(11,200,11):
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == -col:
            possibleMoves.append(position+x)
            break
        if currentBoard[0][position+x] == 99 or currentBoard[0][position+x] == col:
            break

    for x in range(11,200,11):
        if currentBoard[0][position-x] == 0:
            possibleMoves.append(position-x)
        if currentBoard[0][position - x] == -col:
            possibleMoves.append(position - x)
            break
        if currentBoard[0][position-x] == 99 or currentBoard[0][position-x] == col:
            break

    return possibleMoves

def knight_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []

    knightMoves = [(24-1), (24+1), (-24+1),(-24-1),(2+12), (-2+12), (2-12), (-2-12)]

    for x in knightMoves:
        if currentBoard[0][position+x] == 0:
            possibleMoves.append(position+x)
        if currentBoard[0][position+x] == -col:
            possibleMoves.append(position+x)

    return possibleMoves

def queen_moves(currentBoard, position):
    col = currentBoard[0][position]
    piece = currentBoard[1][position]
    possibleMoves = []

    possibleMoves.extend(bishop_moves(currentBoard, position))
    possibleMoves.extend(rook_moves(currentBoard, position))

    return possibleMoves


def make_move(currentBoard, position_from, position_to):
    new_board = [currentBoard[0].copy(), currentBoard[1].copy()]
    new_board[0][position_to] = new_board[0][position_from]
    new_board[1][position_to] = new_board[1][position_from]
    new_board[0][position_from] = 0
    new_board[1][position_from] = 0
    return new_board
i = 0


def get_all_moves(board, col):
    moves = []
    for i in range(144):
        if board[0][i] == col:
            piece_moves = get_moves_for_piece(board, i)  # based on piece type

            if piece_moves is not None:
                for move in piece_moves:
                    if move is not None:
                        moves.append((i, move))
    return moves


def perft(board, depth, color):
    if depth == 0:
        return 1

    nodes = 0
    moves = get_all_moves(board, color)

    for position_from, position_to in moves:

        new_board = make_move(board, position_from, position_to)
        nodes += perft(new_board, depth - 1, -color)

    return nodes


def get_moves_for_piece(board, position):
    match board[1][position]:

        case 1:
            return(pawn_moves(board, position))
        case 6:
            return(king_moves(board, position))
        case 4:
            return(rook_moves(board, position))
        case 3:
            return(bishop_moves(board, position))
        case 2:
            return(knight_moves(board, position))
        case 5:
            return(queen_moves(board, position))
    return None


"""while i<144:

    totalMoves = []
    match currentBoard[1][i]:

        case 1:
            print("Pawn moves:")
            print(pawn_moves(currentBoard, i))
            totalMoves.append(pawn_moves(currentBoard, i))
        case 6:
            print("King moves:")
            print(king_moves(currentBoard, i))
            totalMoves.append(king_moves(currentBoard, i))
        case 4:
            print("Rook moves:")
            print(rook_moves(currentBoard, i))
            totalMoves.append(rook_moves(currentBoard, i))
        case 3:
            print("Bishop moves:")
            print(bishop_moves(currentBoard, i))
            totalMoves.append(bishop_moves(currentBoard, i))
        case 2:
            print("Knight moves:")
            print(knight_moves(currentBoard, i))
            totalMoves.append(knight_moves(currentBoard, i))
        case 5:
            print("Queen moves:")
            print(queen_moves(currentBoard, i))
            totalMoves.append(queen_moves(currentBoard, i))

    i+=1"""

    # Starting position: perft(1)=20, perft(2)=400, perft(3)=8902, etc.
print(f"Perft(1): {perft(startingBoard, 4, -1)}")  # Should be 20 for depth 1
