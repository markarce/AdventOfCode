

def boilerplate(filename):
    with open(filename) as f:
        word = f.readlines()[0]

    chars = list(word)
    print(chars)

    for i in range(len(chars)):
        if len(set(chars[i:i+14])) == 14:
            print(set(chars[i:i+14]))
            print(i + 14)
            return



boilerplate("data.txt")