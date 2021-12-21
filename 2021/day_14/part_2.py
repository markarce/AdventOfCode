from collections import defaultdict, deque

def expand_polymer(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]

    polymer_template = lines[0]
    letter_count = {}
    pair_insertion_rules = {}

    for line in lines[2:]:
        pair, letter = line.split(" -> ")
        letter_count[letter] = 0
        pair_insertion_rules[pair] = {
            "value": letter, "children": [f"{pair[0] + letter}", f"{letter + pair[1]}"]
        }

    print(pair_insertion_rules)
    for char in polymer_template:
        letter_count[char] += 1

    print(letter_count)

    queued_nodes = deque()

    for i in range(0, len(polymer_template) - 1):
                    pair = polymer_template[i: i + 2]
                    print(pair)
                    queued_nodes.append(pair)

    print(queued_nodes)


    time_to_depth_increase = len(queued_nodes)
    depth = 0
    pending_depth_increase = False

    while depth < 40:
        print(f"depth: {depth}")
        node = pair_insertion_rules[queued_nodes.popleft()]
        time_to_depth_increase -= 1
        letter_count[node["value"]] += 1
        if time_to_depth_increase == 0:
            depth += 1
            pending_depth_increase = True
        for child in node["children"]:
            queued_nodes.append(child)
        if pending_depth_increase:
            time_to_depth_increase = len(queued_nodes)
            pending_depth_increase = False

    print(letter_count)
    highest = letter_count[max(letter_count, key=letter_count.get)]
    lowest = letter_count[min(letter_count, key=letter_count.get)]

    print(highest - lowest)
    # print(lines)
    # print(polymer_template)
    # print(pair_insertion_rules)

expand_polymer("sample_data.txt")
