from checkers.constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from checkers.piece import Piece
import copy

depth = 3


def minimax(board, depth, max_player):
    if depth == 0 or board.winner() != None:
        return board.evaluate()

    if max_player:
        max_eval = float('-inf')
        for piece in board.get_valid_pieces(WHITE):
            for (row, col), skip in board.get_valid_moves(piece).items():
                new_board = copy.deepcopy(board)
                new_piece = new_board.get_piece(piece.row, piece.col)
                new_board.move(new_piece, row, col)
                if skip:
                    new_board.remove(skip)
                eval = minimax(new_board, depth-1, False)
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
                eval = minimax(new_board, depth-1, True)
                min_eval = min(min_eval, eval)
        return min_eval


def best_move(board, player):

    # white is the maximizer. it is inverted because the current player's first
    # move happens in this function, so the next player to go is the opponent
    if player == "WHITE":
        max_player = False
    else:
        max_player = True

    # the init best_move needs to be invalid so that it shows no move is possible
    best_move = (Piece(0, 0, WHITE), -9, -9)
    best_score = float('-inf')

    for piece in board.get_valid_pieces(player):
        for (row, col), skip in board.get_valid_moves(piece).items():
            new_board = copy.deepcopy(board)
            new_piece = new_board.get_piece(piece.row, piece.col)
            new_board.move(new_piece, row, col)
            if skip:
                new_board.remove(skip)
            val = minimax(new_board, depth, max_player)

            if val > best_score:
                best_score = val
                best_move = (piece, row, col)

    return best_move
