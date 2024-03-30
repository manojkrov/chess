# Python based UCI chess engine


## Chronological order of functionality added

###
1. Board representation
2. UCI protocol
3. Move generation
4. Evaluation function
5. Negamax search
6. Move ordering
7. Alpha-beta pruning

## Board representation
Board representation is done using pychess library.

## UCI protocol
Basic UCI protocol is implemented.
Commands implemented:
1. uci
2. isready
3. position startpos moves
4. position fen
5. ucinewgame
6. debug
7. go
8. stop
9. quit

For first iteration i just implemented uci and returned a random move as best move.

## Move generation
Move generation is done using pychess library, which provides a list of all possible legal moves from the current position.

## Evaluation function
Evaluation function was implemented using simple material count and positional evaluation from
https://www.chessprogramming.org/Evaluation with centipawn values.

## Negamax search

Negamax search is implemented with ordered moves based on evaluation function.

## Move ordering
Move ordering is done based on ordering the result of the evaluation function of the legal moves possible from the current position.

Depth is set to 3 for now.
The evaluation function has a hashmap to store the evaluation of the position to avoid recomputation of the same position
