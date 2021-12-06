"""--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""

def find_double_overlaps(filename):
    with open(filename) as f:
        lines = f.readlines()

    with open(filename) as file:
        line_list = []
        for line in file:
            start, end = line.split(" -> ")
            start = [int(num) for num in start.split(",")]
            end = [int(num) for num in end.split(",")]
            if start[0] == end[0] or start[1] == end[1]:
                line_list.append([start, end])

    overlaps = {}
    
    for line in line_list: # 2,2 -> 2,1
        start = line[0] # 2,2
        end = line[1] # 2,1

        # check if vertical
        if start[0] == end[0]: # true
            low = min(start[1], end[1]) # 1
            high = max(start[1], end[1]) # 2
            for i in range(low, high + 1):
                point = f"{start[0]},{i}"
                overlaps[point] = overlaps.get(point, 0) + 1

        # check if horizontal
        elif start[1] == end[1]:
            low = min(start[0], end[0]) # 1
            high = max(start[0], end[0]) # 2
            for i in range(low, high + 1):
                point = f"{i},{start[1]}"
                overlaps[point] = overlaps.get(point, 0) + 1

    count = 0
    for key in overlaps.keys():
        if overlaps[key] > 1:
            count += 1

    print(count)

find_double_overlaps("data.txt")