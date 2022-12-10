from collections import deque


def find_sum_of_interesting_signal_strenths(filename):
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

    # 20th, 60th, 100th, 140th, 180th, and 220th cycles
    print(sum([
        output[20 -1] * 20,
        output[60 -1] * 60,
        output[100 -1] * 100,
        output[140 -1] * 140,
        output[180 -1] * 180,
        output[220 -1] * 220,
    ]))

find_sum_of_interesting_signal_strenths("data.txt")