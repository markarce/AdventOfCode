

def boilerplate(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]


boilerplate("sample_data.txt")