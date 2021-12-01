def parse_bag_rules(file_location):  # /Users/marce/AdventOfCode/2020/bag_rules.txt
    import re
    with open(file_location) as f:
        bag_rules = f.read().split(".\n")

    bag_rules[-1] = bag_rules[-1][:-1]
    bag_contents = {}
    for rule in bag_rules:
        container, contents = rule.split("s contain ")
        if contents == "no other bags":
            bag_contents[container] = None

        else:
            contents = contents.split(", ")
            formatted_contents = []
            for bag_count_and_type in contents:
                if bag_count_and_type[-1] == "s":
                    bag_count_and_type = bag_count_and_type[:-1]
                m = re.match(r"(\d+)\s(.*)", bag_count_and_type)
                bag_count = m.group(1)
                bag_type = m.group(2)
                new_contents = {}
                new_contents[bag_type] = bag_count
                formatted_contents.append(new_contents)
            bag_contents[container] = formatted_contents
    return bag_contents

def does_bag_hold_gold_bags(bag, all_bags):
    # empty bag holds no bags
    if all_bags[bag] is not None:
        gold_bags_held = []
        for element in all_bags[bag]:
        # recursive case: bag contains 1 or more bags
            for key in element.keys():
        # one bag is a gold bag
                if key == "shiny gold bag":
                    gold_bags_held.append(True)
                else:
                    gold_bags_held.append(does_bag_hold_gold_bags(key, all_bags))
        return any(gold_bags_held)

def bags_inside_bag(bag, all_bags):
    bags_held = 0
    if all_bags[bag] is not None:
        for element in all_bags[bag]:
            for key in element.keys():
                bags_held += int(element[key])
                bags_held += bags_inside_bag(key, all_bags)
    return bags_held