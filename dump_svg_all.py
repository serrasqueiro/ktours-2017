# dump_svg_all.py
# Generate a minimalistic SVG file for every move in a PGN game.

import os
import chess
import chess.pgn
import chess.svg

SHOW_COORDINATES = True

def main():
    pgn_path = "Caruana_vs_Kasparov_2017.pgn"
    out_dir = "svgs_all_moves"
    show_coords = SHOW_COORDINATES
    exported = script(pgn_path, out_dir, show_coords)
    print(f"Exported {exported} SVG files to {out_dir}")


def script(pgn_path, out_dir, show_coords=False):
    """ Export coordinates into move_N.svg file(s). """
    exported = dump_all_moves_to_svg(
        pgn_path=pgn_path,
        out_dir=out_dir,
        base_name="move",
        size=400,
        coordinates=show_coords,  # True: shows rank/file labels
    )
    return exported


def ensure_dir(path):
    if os.path.isdir(path):
        print("Re-using:", path)
        return False
    os.makedirs(path)
    return True


def svg_for_move(board, last_move=None, size=400, coordinates=False):
    # Minimalistic SVG: no coordinates, no arrows, no labels
    return chess.svg.board(
        board=board,
        lastmove=last_move,
        size=size,
        coordinates=coordinates
    )


def dump_all_moves_to_svg(pgn_path, out_dir, base_name="move", size=400, coordinates=False):
    ensure_dir(out_dir)
    with open(pgn_path, "r", encoding="ascii") as fdin:
        pname = fdin.readlines()[0].strip()
        if pname in ("365chess_games.pgn",):
            pgn_path = pname
    with open(pgn_path, "r", encoding="utf-8") as fdin:
        print("Read:", pgn_path)
        game = chess.pgn.read_game(fdin)
    if game is None:
        raise ValueError("No game found in PGN file.")
    board = game.board()
    move_index = 0
    # Initial position before any move
    svg_init = svg_for_move(board, last_move=None, size=size, coordinates=coordinates)
    init_name = f"{base_name}_{move_index:03d}.svg"
    pname = os.path.join(out_dir, init_name)
    with open(pname, "w", encoding="utf-8") as outf:
        print("(Re-)creating:", out_dir)
        outf.write(svg_init)
    # Iterate through all moves
    for mv in game.mainline_moves():
        print("Move:", mv)
        board.push(mv)
        move_index += 1
        svg_data = svg_for_move(board, last_move=mv, size=size, coordinates=coordinates)
        fname = f"{base_name}_{move_index:03d}.svg"
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as outf:
            outf.write(svg_data)
    return move_index  # number of moves exported


if __name__ == "__main__":
    main()
