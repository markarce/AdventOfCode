"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
"""


def part_1(filename):
    
    def get_digit(side, data):
        if side == "right":
            data = data[::-1]
        for c in data:
            if c.isdigit():
                return int(c)

    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]

    total = 0

    for line in lines:
        print(line)
        number = 10 * get_digit("left", line) + get_digit("right", line)
        total += number

    print(total)


# part_1("data.txt")


def part_2(filename):
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    new_digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]

    pairs = []
    for line in lines:
        print(line)
        line_pairs = []
        for i in range(len(line)):
            print("i = ", i)
            for digit in digits:
                pair = [None, None]
                pair[0] = i
                digit_len = len(digit)
                # print("LOOK:", line[i:i + digit_len])
                if line[i:i + digit_len] == digit:
                    print(digit)
                    pair[1] = new_digits.get(digit)
                    line_pairs.append(pair)
                    # print("appended: ", pair)
        pairs.append(line_pairs)
    print(pairs)
    total = 0
    for pair in pairs:
        total += 10 * pair[0][1] + pair[-1][1]

    print(total)

part_2("data.txt")
