

def boilerplate(filename):
    with open(filename) as f:
        lines = f.readlines()


boilerplate("sample_data.txt")