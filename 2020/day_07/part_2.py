def parse_bag_rules(file_location):  # /Users/marce/AdventOfCode/2020/bag_rules.txt
    from collections import deque


    bag_contents = {}
    with open(file_location) as f:
        for line in f:
            container, contents = line.split("s contain ")
            if contents.rstrip() == "no other bags.":
                bag_contents[container] = None
            else:
                bag_contents[container] = {bag[2:].rstrip("s."): int(bag[:1]) for bag in contents[:-1].split(", ")}

    stack = deque()
    bag_total = 0
    for bag in bag_contents["shiny gold bag"].items():
        stack.append((bag))

    while stack:
        print(stack)
        current_bag, current_count = stack.pop()
        bag_total += current_count
        if bag_contents[current_bag] is not None:
            for i in range(current_count):
                stack.extend(bag for bag in bag_contents[current_bag].items())

    print(bag_total)

parse_bag_rules("bag_rules.txt")