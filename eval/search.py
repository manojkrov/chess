from eval.eval import evaluate  # noqa
from eval.movegen import generate_next_moves
from config.config import best_move, total_moves_evaluated
from prettyprint import PrettyPrintTree
from chess import Board
from chess import Move
from colorama import Back

pt = PrettyPrintTree(lambda x: x.children, lambda x: str(x.move)+":"+str(x.score), orientation=PrettyPrintTree.Horizontal, color=Back.MAGENTA)


class Tree:
    def __init__(self, score, move: Move, turn):
        self.score = score
        self.move = move
        self.turn = turn
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return child


def think(board, depth):
    global best_move
    global total_moves_evaluated
    tree = Tree(0, board.peek(), board.turn)
    best_score = -100000
    alpha = -100000
    beta = 100000
    moves_list = generate_next_moves(board)
    while len(moves_list) > 0:
        move = max(moves_list, key=moves_list.get)
        total_moves_evaluated += 1
        if not board.is_legal(move):
            del moves_list[move]
            continue
        board.push(move)
        score = -negamax(board, depth - 1, alpha, beta)
        board.pop()
        del moves_list[move]
        if score > best_score:
            best_score = score
            best_move = move
    print(f"Total moves evaluated: {total_moves_evaluated}")
    #pt(tree)
    return best_move


def negamax(board, depth, alpha, beta):
    global total_moves_evaluated
    if depth == 0:
        evaluation = evaluate(board) if board.turn else -evaluate(board)
        return evaluation

    score = -100000
    for move in generate_next_moves(board):
        total_moves_evaluated += 1
        board.push(move)
        score = max(score, -negamax(board, depth - 1, -beta, -alpha))
        #score = -negamax(board, depth - 1, -beta, -alpha, child)
        board.pop()
        alpha = max(score, alpha)
        if alpha >= beta:
            break
    return score
