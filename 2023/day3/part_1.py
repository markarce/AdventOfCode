"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

from functools import reduce


def part_1(filename):
    symbols = set(['#', '$', '%', '&', '*', '+', '-', '/', '=', '@'])

    def is_valid_position(matrix, row, col):
        if (row < 0 or col < 0 or row > len(matrix) - 1 or col > len(matrix[0]) - 1):
            return False
        return True

    def get_and_remove_number(matrix, row, col):
        left = col
        right = col
        while is_valid_position(matrix, row, left) and matrix[row][left].isdigit():
            print("LEFT matrix, left", left)
            print(matrix[row][left])
            if is_valid_position(matrix, row, left - 1) and matrix[row][left - 1].isdigit():
                left -= 1
            else:
                print("FINAL LEFT: ", left)
                break
        while is_valid_position(matrix, row, right) and matrix[row][right].isdigit():
            print("RIGHT matrix, right", right)
            print(matrix[row][right])
            if is_valid_position(matrix, row, right + 1) and matrix[row][right + 1].isdigit():
                right += 1
            else:
                print("FINAL RIGHT: ", right)
                break
        number = matrix[row][left:right + 1]
        for j in range(left, right + 1):
            matrix[row][j] = "."
        number = "".join(number)
        print("NUMBER: ", number)
        return number
        

    def get_adjacent_numbers(matrix, row, col):
        numbers = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if is_valid_position(matrix, i, j) and matrix[i][j] != "." and matrix[i][j] not in symbols:
                    print("calling get and remove: ", i, j)
                    number = get_and_remove_number(matrix, i, j)
                    numbers.append(int(number))

        return numbers


    with open(filename) as f:
        lines = [list(line.rstrip()) for line in f.readlines()]

    numbers = []

    for row in lines:
        print(*row)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] in symbols:
                print("symbol here:", lines[i][j])
                print("checking: ", i, j)
                numbers.extend(get_adjacent_numbers(lines, i, j))

    print(sum(numbers))

# part_1("data.txt")

"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""


def part_2(filename):
    symbols = set(['#', '$', '%', '&', '*', '+', '-', '/', '=', '@'])
    def is_valid_position(matrix, row, col):
        if (row < 0 or col < 0 or row > len(matrix) - 1 or col > len(matrix[0]) - 1):
            return False
        return True

    def get_and_remove_number(matrix, row, col):
        left = col
        right = col
        while is_valid_position(matrix, row, left) and matrix[row][left].isdigit():
            print("LEFT matrix, left", left)
            print(matrix[row][left])
            if is_valid_position(matrix, row, left - 1) and matrix[row][left - 1].isdigit():
                left -= 1
            else:
                print("FINAL LEFT: ", left)
                break
        while is_valid_position(matrix, row, right) and matrix[row][right].isdigit():
            print("RIGHT matrix, right", right)
            print(matrix[row][right])
            if is_valid_position(matrix, row, right + 1) and matrix[row][right + 1].isdigit():
                right += 1
            else:
                print("FINAL RIGHT: ", right)
                break
        number = matrix[row][left:right + 1]
        for j in range(left, right + 1):
            matrix[row][j] = "."
        number = "".join(number)
        print("NUMBER: ", number)
        return number
        

    def get_adjacent_numbers(matrix, row, col):
        numbers = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if is_valid_position(matrix, i, j) and matrix[i][j] != "." and matrix[i][j] not in symbols:
                    print("calling get and remove: ", i, j)
                    number = get_and_remove_number(matrix, i, j)
                    numbers.append(int(number))
        if len(numbers) == 2:
            return reduce(lambda x, y: x*y, numbers)


    with open(filename) as f:
        lines = [list(line.rstrip()) for line in f.readlines()]

    numbers = []

    for row in lines:
        print(*row)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "*":
                print("symbol here:", lines[i][j])
                print("checking: ", i, j)
                number = get_adjacent_numbers(lines, i, j)
                if number:
                    numbers.append(number)

    print(sum(numbers))

part_2("data.txt")
