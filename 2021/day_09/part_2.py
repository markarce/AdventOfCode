"""--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 506.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678
The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678
The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

"""
from functools import reduce
    

def multiply_sizes_of_three_largest_basins(filename):
    pp = pprint.PrettyPrinter(indent=4)
    with open(filename) as f:
        lines = [[int(num) for num in line.rstrip()] for line in f.readlines()]

    lowest_points = []

    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            print(lines[i][j])
            total = 0
            count = 0

            if i > 0:
                # check above
                total += 1
                if lines[i][j] < lines[i - 1][j]:
                    count += 1
            if j > 0:
                # check left
                total += 1
                if lines[i][j] < lines[i][j - 1]:
                    count += 1
            if i < len(lines) - 1:
                # check below
                total += 1
                if lines[i][j] < lines[i + 1][j]:
                    count += 1
            if j < len(lines[i]) - 1:
                # check right
                total += 1
                if lines[i][j] < lines [i][j + 1]:
                    count += 1
            if count == total:
                lowest_points.append([i, j])

    print(f"lowest_points: {lowest_points}")
    basin_sizes = []
    
    def get_basin_info(i, j, basin):
        basin[f"{i},{j}"] = lines[i][j]
        places_to_check = []

        if i > 0 and lines[i - 1][j] != 9:
            if f"{i - 1},{j}" not in basin.keys():
                places_to_check.append((i - 1,j))
        if i < len(lines) - 1 and lines[i + 1][j] != 9:
            if f"{i + 1},{j}" not in basin.keys():
                places_to_check.append((i + 1,j))
        if j > 0 and lines[i][j - 1] != 9:
            if f"{i},{j - 1}" not in basin.keys():
                places_to_check.append((i,j - 1))
        if j < len(lines[0]) - 1 and lines[i][j + 1] != 9:
            if f"{i},{j + 1}" not in basin.keys():
                places_to_check.append((i,j + 1))
        
        for place in places_to_check:
            get_basin_info(*place, basin)

        
    for point in lowest_points:
        i = point[0]
        j = point[1]
        basin = {}

        get_basin_info(point[0], point[1], basin)
        basin_sizes.append(len(basin))


    print(f"basin_sizes: {reduce(lambda x, y: x*y, sorted(basin_sizes)[:-4:-1])}")

multiply_sizes_of_three_largest_basins("data.txt")