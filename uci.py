import sys
import chess
import argparse
from config.config import position_score_dict
from config.config import position_ordered_moves_dict
from config.config import best_move
from config.config import total_moves_evaluated
from eval.search import think


def uci():
    """
    The main input/output loop.
    This implements a part of the UCI protocol.
    """
    board = chess.Board()

    while True:
        input_command = input()
        command(board, input_command)


def command(board: chess.Board, input_command: str):
    global best_move
    """
    Accept UCI commands and respond.
    The board state is also updated.
    """
    input_command = input_command.strip()
    tokens = input_command.split(" ")
    while "" in tokens:
        tokens.remove("")

    if input_command == "quit":
        sys.exit()

    if input_command == "uci":
        print("id name Manchess")
        print("id author Manoj Krovvidi")
        print("uciok")
        return

    if input_command == "isready":
        print("readyok")
        return

    if input_command == "ucinewgame":
        position_ordered_moves_dict.clear()
        position_score_dict.clear()
        best_move = None

        return

    if input_command == "stop":
        print(f"bestmove {best_move}")
        return
    if input_command.startswith("position"):
        if len(tokens) < 2:
            return

        # Set starting position
        if tokens[1] == "startpos":
            board.reset()
            moves_start = 2
        elif tokens[1] == "fen":
            fen = " ".join(tokens[2:8])
            board.set_fen(fen)
            moves_start = 8
        else:
            return

        current_fen = board.fen()
        # Add moves
        if len(tokens) <= moves_start or tokens[moves_start] != "moves":
            return

        for move in tokens[(moves_start+1):]:
            if not board.is_legal(chess.Move.from_uci(move)):
                print(f"info string Illegal move: {move}")
                board.set_fen(current_fen)
                break
            board.push_uci(move)

    if input_command == "d":
        # Non-standard command, but supported by Stockfish and helps debugging
        print(board)
        print(board.fen())
        board.push(chess.Move.null())

    if input_command[0:2] == "go":
        depth = 3
        board.is_checkmate()
        if len(tokens) > 1 and tokens[1] == "depth":
            depth = int(tokens[2])
        print(f"bestmove {think(board, depth)}")
        return
