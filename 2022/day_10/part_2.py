from collections import deque


def draw_letters(filename):
    with open(filename) as f:
        queue = deque([line.rstrip() for line in f.readlines()])

    X = 1
    position = 0
    output = [None] * 241
    output[0] = 1
    while queue:
        instruction = queue.popleft()
        position += 1
        output[position] = X
        if instruction.startswith("addx"):
            addx_value = instruction.split(" ")[1]
            position += 1
            X += int(addx_value)
            output[position] = X

    def draw_pixel(matrix, row, column, sprite):
        if sprite[column] == "#":
            matrix[row][column] = "#"
        else:
            matrix[row][column] = "."

    def draw_sprite(x_value):
        sprite = ["."] * 45
        sprite[x_value - 1] = "#"
        sprite[x_value + 0] = "#"
        sprite[x_value + 1] = "#"
        return sprite

    screen = [["."]* 40 for _ in range(6)]

    sprite = draw_sprite(1)
    print(output)
    for i in range(240):
        sprite = draw_sprite(output[i])
        draw_pixel(screen, i // 40, i % 40, sprite)

    for i in range(6):
        print("".join(screen[i]))

draw_letters("data.txt")