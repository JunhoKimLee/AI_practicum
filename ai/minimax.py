from checkers.constants import RED, WHITE
from checkers.piece import Piece
import copy
import random


def minimax(board, depth, max_player, h, parameters):
    if depth == 0 or board.winner() != None:
        if h == 0:
            return board.evaluate()
        elif h == 1:
            return board.evaluate1(parameters)

    if max_player:
        max_eval = float('-inf')
        for piece in board.get_valid_pieces(WHITE):
            for (row, col), skip in board.get_valid_moves(piece).items():
                new_board = copy.deepcopy(board)
                new_piece = new_board.get_piece(piece.row, piece.col)
                new_board.move(new_piece, row, col)
                if skip:
                    new_board.remove(skip)
                eval = minimax(new_board, depth-1, False, h, parameters)
                max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for piece in board.get_valid_pieces(RED):
            for (row, col), skip in board.get_valid_moves(piece).items():
                new_board = copy.deepcopy(board)
                new_piece = new_board.get_piece(piece.row, piece.col)
                new_board.move(new_piece, row, col)
                if skip:
                    new_board.remove(skip)
                eval = minimax(new_board, depth-1, True, h, parameters)
                min_eval = min(min_eval, eval)
        return min_eval


def best_move(board, player, heuristic, parameters):

    # first break down heuristic into heuristic # and depth
    if heuristic < 10:
        h = 0
        depth = heuristic
    else:
        h = int((heuristic - (heuristic % 10))/10)
        depth = heuristic % 10

    # white is the maximizer. it is inverted because the current player's first
    # move happens in this function, so the next player to go is the opponent
    if player == WHITE:
        max_player = False
    else:
        max_player = True

    # the init best_move needs to be invalid so that it shows no move is possible
    best_move = (Piece(0, 0, WHITE), -9, -9)
    if player == WHITE:
        best_score = float('-inf')
    else:
        best_score = float('inf')

    # shuffle for less likely draw
    pieces = board.get_valid_pieces(player)
    random.shuffle(pieces)

    for piece in pieces:
        for (row, col), skip in board.get_valid_moves(piece).items():
            new_board = copy.deepcopy(board)
            new_piece = new_board.get_piece(piece.row, piece.col)
            new_board.move(new_piece, row, col)
            if skip:
                new_board.remove(skip)
            val = minimax(new_board, depth-1, max_player, h, parameters)

            # need to min or max depending on player color
            if player == WHITE:
                if val > best_score:
                    best_score = val
                    best_move = (piece, row, col)
            else:
                if val < best_score:
                    best_score = val
                    best_move = (piece, row, col)

    return best_move
