import collections

import chess
from eval.eval import evaluate
from config.config import position_ordered_moves_dict
from collections import OrderedDict


def generate_next_moves(board: chess.Board):
    """
    Generate all legal moves for the given board sorted by most valuable immediate move
    """
    global position_ordered_moves_dict
    if position_ordered_moves_dict.get(hash(board.fen())):  # Check if the position is already evaluated
        return position_ordered_moves_dict[hash(board.fen())]

    pseudo_legal_moves = list(board.pseudo_legal_moves)

    moves_with_weights = OrderedDict()
    for move in pseudo_legal_moves:
        board.push(move)
        move.weight = evaluate(board)
        board.pop()
        moves_with_weights[move] = move.weight
    turn = board.turn
    # ordered_moves = collections.OrderedDict(sorted(moves_with_weights.items(), key=lambda item: item[1], reverse=turn))
    position_ordered_moves_dict[hash(board.fen())] = moves_with_weights
    # return list(ordered_moves.keys())
    return moves_with_weights

