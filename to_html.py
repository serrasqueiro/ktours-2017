"""
to_html.py
Collect all SVG files and generate a simple HTML viewer to step through moves.
"""

import os


def main():
    svg_dir = "svgs_all_moves"  # directory containing move_000.svg, move_001.svg, ...
    do_script(svg_dir)


def do_script(svg_dir):
    """ Main stuff! """
    res = build_html(svg_dir, output_html="index.html")
    output_html, html_lines, svg_files = res
    assert html_lines, "html_lines"
    print(f"HTML viewer written to {output_html}:", svg_files)


def build_html(svg_dir, output_html="index.html"):
    # Collect all SVG files in order
    svg_files = sorted([f for f in os.listdir(svg_dir) if f.endswith(".svg")])
    # Convert Python list into proper JavaScript array
    str_moves = ",".join(f'"{svg_dir}/{f}"' for f in svg_files)
    moves_js = "[" + str_moves + "]"
    # Build HTML content
    html_lines = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "  <meta charset='UTF-8'>",
        "  <title>Kasparov vs Caruana – SVG Viewer</title>",
        "  <style>",
        "    body { font-family: sans-serif; text-align: center; }",
        "    img { border: 1px solid #ccc; margin: 10px; }",
        "    .controls { margin: 20px; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>Kasparov vs Caruana – Saint Louis Blitz 2017</h1>",
        "  <div class='controls'>",
        "    <button onclick='prevMove()'>Previous</button>",
        "    <button onclick='nextMove()'>Next</button>",
        "    <button onclick='toggleAutoPlay()'>Auto Play</button>",
        "    <p id='moveLabel'></p>",
        "  </div>",
        "  <div>",
        "    <img id='board' src='' alt='Chess board'>",
        "  </div>",
        "  <script>",
        f"    const moves = {moves_js};",
        "    let index = 0;",
        "    let autoPlayInterval = null;",
        "",
        "    function showMove(i) {",
        "      document.getElementById('board').src = moves[i];",
        "      document.getElementById('moveLabel').innerText = 'Move ' + i;",
        "    }",
        "",
        "    function prevMove() {",
        "      if (index > 0) { index--; showMove(index); }",
        "    }",
        "",
        "    function nextMove() {",
        "      if (index < moves.length - 1) { index++; showMove(index); }",
        "    }",
        "",
        "    function toggleAutoPlay() {",
        "      if (autoPlayInterval) {",
        "        clearInterval(autoPlayInterval);",
        "        autoPlayInterval = null;",
        "      } else {",
        "        autoPlayInterval = setInterval(() => {",
        "          if (index < moves.length - 1) {",
        "            index++;",
        "            showMove(index);",
        "          } else {",
        "            clearInterval(autoPlayInterval);",
        "            autoPlayInterval = null;",
        "          }",
        "        }, 2000); // advance every 2 seconds",
        "      }",
        "    }",
        "",
        "    // Initialize",
        "    showMove(index);",
        "  </script>",
        "</body>",
        "</html>"
    ]
    with open(output_html, "w", encoding="utf-8") as f:
        f.write("\n".join(html_lines) + "\n")
    return output_html, html_lines, svg_files


if __name__ == "__main__":
    main()
