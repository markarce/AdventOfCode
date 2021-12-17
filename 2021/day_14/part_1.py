from collections import defaultdict

def expand_polymer(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]


    polymer_template = lines[0]

    pair_insertion_rules = {}
    for line in lines[2:]:
        pair, letter = line.split(" -> ")
        pair_insertion_rules[pair] = letter

    def process_polymer(polymer, steps):
        while steps > 0:
            new_polymer = ""
            last = polymer[-1]
            print(polymer)
            print(last)
            for i in range(0, len(polymer) - 1):
                pair = polymer[i: i + 2]
                print(pair)
                new_polymer += polymer[i] + pair_insertion_rules[pair]
            new_polymer += last
            print(new_polymer)
            polymer = new_polymer
            steps -= 1
        return polymer

    print(pair_insertion_rules)

    polymer = process_polymer(polymer_template, 10)

    letter_count = defaultdict(lambda: 0)

    for letter in polymer:
        letter_count[letter] += 1

    print(letter_count)
    highest = letter_count[max(letter_count, key=letter_count.get)]
    lowest = letter_count[min(letter_count, key=letter_count.get)]

    print(highest - lowest)
    # print(lines)
    # print(polymer_template)
    # print(pair_insertion_rules)

expand_polymer("sample_data.txt")
