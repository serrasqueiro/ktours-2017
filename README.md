## Kasparov vs Caruana -- Saint Louis Blitz 2017

This repository contains a Python script and assets to visualize the **final position** of the game  
Caruana vs Kasparov, Saint Louis Blitz 2017 (Round 12.3, ECO B23).

## Files
- `dump_svg_last.py` -> Python script that reads the PGN and generates a PNG of the last move.
- `Caruana_vs_Kasparov_2017.pgn` -> PGN file with the full game.
- `kasparov_last_move.png` -> Output image showing the final board position with Kasparov's last move highlighted.

## Usage
### 1. Install dependencies
```bash
pip install chess cairosvg
```

### 2. Generate images
```bash
python dump_svg_all.py
```

### 3. Generate index.html:
   + `python to_html.py`

# Other sweets!

## Probable Continuation (illustrative)

Although Caruana resigned after **65... Rh2+**, a likely continuation could have been:

| Move | White (Caruana) | Black (Kasparov) | Comment |
|------|-----------------|------------------|---------|
| 66   | Kg1             | Rh1+             | Black rook drives king further into the corner |
| 67   | Kg2             | Ne3+             | Knight joins the attack with tempo |
| 68   | Kf2             | Rf1+             | Rook check, forcing king back |
| 69   | Ke2             | Rf2+             | Rook invades, tightening the net |
| 70   | Kxf2            | Nxf5             | Knight recaptures, maintaining material edge |
| 71   | gxf5            | Kg7              | Black king centralizes, ready to support pawns |
| 72   | Kg3             | Kf6              | King marches forward |
| 73   | Kg4             | h5+              | Pawn thrust, opening mating net |
| 74   | Kxh5            | Kxf5             | King captures but Black king dominates |
| 75   | h4              | Rh8#             | Final rook mate on h8 |

**Result:** 0–1 (Kasparov checkmates)
