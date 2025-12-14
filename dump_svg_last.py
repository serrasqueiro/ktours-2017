""" kasparov_last_move_png.py
Generate a PNG image of the final position from Caruana vs Kasparov (Saint Louis Blitz 2017)
"""

import chess
import chess.pgn
import chess.svg
import cairosvg


def main():
    # Replace with your PGN file path
    pgn_file = "Caruana_vs_Kasparov_2017.pgn"
    output_png = "kasparov_last_move.png"
    script(pgn_file, output_png)


def script(pgn_file, output_png):
    generate_last_position_png(pgn_file, output_png)


def generate_last_position_png(pgn_file, output_png):
    # Load the PGN file
    with open(pgn_file, "r", encoding="utf-8") as f:
        game = chess.pgn.read_game(f)
    # Play through the game to the end
    board = game.board()
    for move in game.mainline_moves():
        board.push(move)

    # Get the last move
    last_move = board.peek()
    print("Last move played:", last_move)

    # Create SVG highlighting the last move
    svg_data = chess.svg.board(board, lastmove=last_move, size=400)

    # Convert SVG to PNG
    cairosvg.svg2png(bytestring=svg_data.encode("utf-8"), write_to=output_png)
    print(f"Final position saved as {output_png}")

def main():
    # Replace with your PGN file path
    pgn_file = "Caruana_vs_Kasparov_2017.pgn"
    output_png = "kasparov_last_move.png"
    generate_last_position_png(pgn_file, output_png)

if __name__ == "__main__":
    main()
