import chess as chess
from config.config import position_score_dict


def evaluate(board: chess.Board):
    """
    Calculate the weight of a move.
    """
    global position_score_dict
    if board.is_checkmate():  # Checkmate
        return -1000000 if board.turn else 1000000

    if position_score_dict.get(hash(board.fen())):
        return position_score_dict[hash(board.fen())]

    temp_board = board
    material_score = calculate_material_score(temp_board)
    mobility_score = calculate_mobility_score(temp_board)
    score = material_score + (mobility_score * 10)
    position_score_dict[hash(temp_board.fen())] = score
    return score


def calculate_mobility_score(temp_board):
    """
    Calculate the mobility score for the given board and color.
    """
    temp_board_turn = temp_board.turn
    temp_board.turn = chess.WHITE
    mobility_white = len(list(temp_board.legal_moves))
    temp_board.turn = chess.BLACK
    mobility_black = len(list(temp_board.legal_moves))
    temp_board.turn = temp_board_turn
    return mobility_white - mobility_black


def piece_score(piece, temp_board):
    """
    Calculate the score of the pieces for the given color.
    """
    return len(list(temp_board.pieces(piece, chess.WHITE))) - \
        len(list(temp_board.pieces(piece_type=piece, color=chess.BLACK)))


def calculate_material_score(temp_board: chess.Board):
    """
    Calculate the score of the pieces for the given color.
    """
    score = 0
    score += 100 * piece_score(chess.PAWN, temp_board)
    score += 320 * piece_score(chess.KNIGHT, temp_board)
    score += 330 * piece_score(chess.BISHOP, temp_board)
    score += 500 * piece_score(chess.ROOK, temp_board)
    score += 900 * piece_score(chess.QUEEN, temp_board)
    score += 20000 * piece_score(chess.KING, temp_board)
    return score
