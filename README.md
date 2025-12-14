## Kasparov vs Caruana -- Saint Louis Blitz 2017

This repository contains a Python script and assets to visualize the **final position** of the game  
Caruana vs Kasparov, Saint Louis Blitz 2017 (Round 12.3, ECO B23).

## Files
- `dump_svg_last.py` -> Python script that reads the PGN and generates a PNG of the last move.
- `Caruana_vs_Kasparov_2017.pgn` -> PGN file with the full game.
- `kasparov_last_move.png` -> Output image showing the final board position with Kasparov's last move highlighted.

## Usage
1. Install dependencies:
```bash
pip install chess cairosvg
python dump_svg_last.py
```
