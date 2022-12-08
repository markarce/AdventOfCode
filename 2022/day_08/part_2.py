from functools import reduce


def boilerplate(filename):
    with open(filename) as f:
        lines = [list(line.rstrip()) for line in f.readlines()]

    scenic_score = 0

    def tree_count_top(lines, j, i):
        tree = lines[j][i]
        count = 0
        while i > 0:
            next_position = lines[j][i-1]
            if tree <= next_position:
                return count + 1
            else:
                count += 1
            i -= 1
        return count

    def tree_count_bottom(lines, j, i):
        tree = lines[j][i]
        count = 0
        while i < len(lines) - 1:
            next_position = lines[j][i+1]
            if tree <= next_position:
                return count + 1
            else:
                count += 1
            i += 1
        return count

    def tree_count_left(lines, j, i):
        tree = lines[j][i]
        count = 0
        while j > 0:
            next_position = lines[j-1][i]
            if tree <= next_position:
                return count + 1
            else:
                count += 1
            j -= 1
        return count

    def tree_count_right(lines, j, i):
        tree = lines[j][i]
        count = 0
        while j < len(lines[i]) - 1:
            next_position = lines[j+1][i]
            if tree <= next_position:
                return count + 1
            else:
                count += 1
            j += 1
        return count

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            scenic_score = max(
                reduce(lambda x, y: x*y, [
                    tree_count_top(lines, j, i),
                    tree_count_bottom(lines, j, i),
                    tree_count_left(lines, j, i),
                    tree_count_right(lines, j, i),
                ]), 
                scenic_score
            )

    print(scenic_score)


boilerplate("data.txt")