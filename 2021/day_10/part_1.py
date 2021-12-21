

def boilerplate(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]

    open_brackets = ["(", "[", "{", "<",]
    close_brackets = [")", "]", "}", ">",]
    corrupt_chars = []

    def note_if_corrupt(line):
        brackets = []
        for i in range(0, len(line)):
            if line[i] in open_brackets:
                brackets.append(line[i])
            else:
                index = close_brackets.index(line[i])
                if open_brackets[index] == brackets[-1]:
                    brackets.pop()
                else:
                    corrupt_chars.append(line[i])
                    return

    for line in lines:
        note_if_corrupt(line)

    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,    
    }

    total_score = 0
    for char in corrupt_chars:
        total_score += scores[char]


boilerplate("sample_data.txt")