import re
from collections import defaultdict


def find_top_crates(filename):
    with open(filename) as f:
        lines = [line for line in f.readlines()]
    # initialize starting stacks
    stacks = defaultdict(list)
    for i in range(1, 10):
        stacks[i] = []
    columns = [1 + i * 4 for i in range(9)]
    for line in lines[:9]:
        for i in range(len(columns)):
            if line[columns[i]].isupper():
                stacks[i + 1].insert(0, line[columns[i]])
    # start after instructions begin on line 11
    for instruction in lines[10:]:
        moves, source, destination = [int(num) for num in re.findall(r'\d+', instruction)]
        crates = stacks[source][-moves:]
        stacks[source] = stacks[source][:-moves]
        stacks[destination].extend(crates)

    print("".join([stack[-1] for stack in stacks.values()]))

find_top_crates("data.txt")