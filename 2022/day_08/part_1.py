

def boilerplate(filename):
    with open(filename) as f:
        lines = [list(line.rstrip()) for line in f.readlines()]

    visible = 0

    def is_visible_top(lines, j, i):
        tree = lines[j][i]
        while i > 0:
            next_position = lines[j][i-1]
            if tree <= next_position:
                return False
            i -= 1
        return True

    def is_visible_bottom(lines, j, i):
        tree = lines[j][i]
        while i < len(lines) - 1:
            next_position = lines[j][i+1]
            if tree <= next_position:
                return False
            i += 1
        return True

    def is_visible_left(lines, j, i):
        tree = lines[j][i]
        while j > 0:
            next_position = lines[j-1][i]
            if tree <= next_position:
                return False
            j -= 1
        return True

    def is_visible_right(lines, j, i):
        tree = lines[j][i]
        while j < len(lines[i]) - 1:
            next_position = lines[j+1][i]
            if tree <= next_position:
                return False
            j += 1
        return True

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if any([
                is_visible_top(lines, j, i),
                is_visible_bottom(lines, j, i),
                is_visible_left(lines, j, i),
                is_visible_right(lines, j, i),
            ]):
                visible += 1

    print(visible)


boilerplate("data.txt")