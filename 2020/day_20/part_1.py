"""--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?
"""

def assemble_tiles_into_image(filename, is_test_data):
    import re
    if not is_test_data:
        with open(filename) as f:
            tiles = f.read().split("\n\n")
    else:
        tiles = filename.split("\n\n")

    print(len(tiles))

    print(tiles[0])

    processed_tiles = []

    # list("".join(expression.split()))

    for tile in tiles:
        processed_tile = tile.split("\n")
        tile_id = int(re.search(r"\d{4}", processed_tile[0]).group(0))
        top_edge = list("".join(processed_tile[1].split()))
        bottom_edge = list("".join(processed_tile[10].split()))
        right_edge = []
        left_edge = []
        for row in range(1, len(processed_tile)):
            left_edge.append(processed_tile[row][0])
            right_edge.append(processed_tile[row][len(processed_tile[0]) - 1])

        tile_dict = {
            "tile_id": tile_id,
            "top_edge": top_edge,
            "bottom_edge": bottom_edge,
            "right_edge": right_edge,
            "left_edge": left_edge,
            "orig_image": processed_tile[1:],
            "flipped": set(),
            "rotated": 0,
        }
        processed_tiles.append(tile_dict)

def flip_tile_horizontally(tile):
    new_top = tile["top_edge"][::-1]
    new_bottom = tile["bottom_edge"][::-1]
    new_left = tile["right_edge"]
    new_right = tile["left_edge"]
    tile["top_edge"] = new_top
    tile["bottom_edge"] = new_bottom
    tile["left_edge"] = new_left
    tile["right_edge"] = new_right
    if "h" not in tile["flipped"]:
        tile["flipped"].add("h")
    else:
        tile["flipped"].remove("h")


def flip_tile_vertically(tile):
    new_top = tile["bottom_edge"]
    new_bottom = tile["top_edge"]
    new_left = tile["left_edge"][::-1]
    new_right = tile["right_edge"][::-1]
    tile["top_edge"] = new_top
    tile["bottom_edge"] = new_bottom
    tile["left_edge"] = new_left
    tile["right_edge"] = new_right
    if "v" not in tile["flipped"]:
        tile["flipped"].add("v")
    else:
        tile["flipped"].remove("v")

def rotate_tile_clockwise(tile):
    new_top = tile["left_edge"][::-1]
    new_bottom = tile["right_edge"][::-1]
    new_left = tile["bottom_edge"]
    new_right = tile["top_edge"]
    tile["top_edge"] = new_top
    tile["bottom_edge"] = new_bottom
    tile["left_edge"] = new_left
    tile["right_edge"] = new_right
    tile["rotated"] += 90
    if tile["rotated"] == 360:
        tile["rotated"] == 0
