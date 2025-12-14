""" # dump_svg_all.py -- including variations.

Generate SVGs for every move in a PGN game, including variation continuation.
"""

import os
import chess
import chess.pgn
import chess.svg

SHOW_COORDINATES = True

def main():
    pgn_path = "365chess_games.pgn"  # Caruana_vs_Kasparov_2017.pgn is a soft-link to that
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
        coordinates=show_coords
    )
    return exported

def ensure_dir(path):
    if os.path.isdir(path):
        print("Re-using:", path)
        return False
    os.makedirs(path)
    return True


def svg_for_move(board, last_move=None, size=400, coordinates=False):
    return chess.svg.board(
        board=board,
        lastmove=last_move,
        size=size,
        coordinates=coordinates
    )


def dump_all_moves_to_svg(pgn_path, out_dir, base_name="move", size=400, coordinates=False, verbose=0):
    print("Read:", pgn_path)
    ensure_dir(out_dir)
    with open(pgn_path, "r", encoding="utf-8") as fdin:
        game = chess.pgn.read_game(fdin)
    if game is None:
        raise ValueError("No game found in PGN file.")
    board = game.board()
    move_index = 0
    # Initial position
    svg_init = svg_for_move(board, last_move=None, size=size, coordinates=coordinates)
    init_name = f"{base_name}_{move_index:03d}.svg"
    with open(os.path.join(out_dir, init_name), "w", encoding="utf-8") as outf:
        print("(Re-)creating:", out_dir)
        outf.write(svg_init)
    # Export mainline moves
    for mv in game.mainline_moves():
        if verbose > 0:
            print("Move:", mv)
        board.push(mv)
        move_index += 1
        svg_data = svg_for_move(board, last_move=mv, size=size, coordinates=coordinates)
        fname = f"{base_name}_{move_index:03d}.svg"
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as outf:
            outf.write(svg_data)
    # Export variation continuation if present
    terminal = game.end()
    if terminal.variations:
        print("Found variation continuation; exporting hypothetical line...")
        var_node = terminal.variations[0]
        while var_node is not None:
            mv = var_node.move
            if mv is None:
                break
            print("Var move:", mv)
            board.push(mv)
            move_index += 1
            svg_data = svg_for_move(board, last_move=mv, size=size, coordinates=coordinates)
            fname = f"{base_name}_{move_index:03d}.svg"
            with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as outf:
                outf.write(svg_data)
            var_node = var_node.variations[0] if var_node.variations else None
    return move_index


if __name__ == "__main__":
    main()
