This is a little tool to generate chessboards from a fen description (see
http://en.wikipedia.org/wiki/Forsyth–Edwards_Notation). You can invoke it
either as a library or from the command line.

Invoking from the command line:
*******************************

python fen.py "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR" --outfile chessboard.png

Call as a library:
******************

import fen
im = draw_board(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
im.save('file.png')