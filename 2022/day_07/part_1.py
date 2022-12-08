"""
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.
Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
"""
from collections import deque, defaultdict


def find_size_of_directories_over_10000(filename):
    with open(filename) as f:
        lines = deque([line.rstrip() for line in f.readlines()])

    print(lines)


# example directory:

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)


    # self.sample_directory = {
    #     "a": {
    #         "e": {
    #             "i": 584,
    #         "f": 29116,
    #         "g": 2557,
    #         "h.lst": 62596,
    #         },
    #     },
    #     "b.txt": 14848514,
    #     "c.dat": 8504156,
    #     "d": {
    #         "j": 4060174,
    #         "d.log": 8033020,
    #         "d.ext": 5626152,
    #         "k": 7214296,
    #     },
    # }


    class Filesystem():
        def __init__(self, lines):
            self.directory = {}
            self.lines = deque(lines)
            self.current_path = [self.directory]

        def cd(self, path):
            print(f"executing cd with argument: {path}")
            print(f"current_full_path: {self.current_path}")
            print(f"current directory structure: {self.directory}")
            if path == "/":
                self.current_path = [self.directory]

            elif path == "..":
                self.current_path.pop()

            else:
                print(f"else, last item in current_path: {self.current_path[-1]}")
                if path in self.current_path[-1].keys():
                    print(f"self.current_path[-1]: {self.current_path[-1]}")
                    self.current_path.append(self.current_path[-1][path])
                else:
                    print("shouldn't be here")

            print(f"new_full_path: {self.current_path}")

        def ls(self):
            if self.lines and not self.lines[0].startswith("$"):
                next_line = self.lines.popleft()
                if next_line.startswith("dir"):
                    # create a directory in self.directory and append the dir
                    name = next_line.split(" ")[1]
                    self.current_path[-1][name] = {}
                    self.ls()
                else:
                    size, filename = next_line.split(" ")
                    self.current_path[-1][filename] = int(size)
                    self.ls()
            return


        def read_lines(self):
            while self.lines:
                line = self.lines.popleft()
                print(line)
                if line.startswith("$"):
                    command = line.split(" ")
                    if command[1] == "cd":
                        self.cd(command[2])
                    elif command[1] == "ls":
                        self.ls()

    def count_directory_sizes(directory):
        # totals = {
        #     ("root",): 
        #     "a": [94853]
        #     "e": [584]
        #     "d": [24933642]
        # }
        totals = defaultdict(list)
        def dfs(node, parent=("root",)):
            for key in node.keys():
                print(key)
                if type(node[key]) == dict:
                    totals[parent].append(key)
                    dfs(node[key], parent=key)
                else:
                    totals[parent].append(node[key])

        # def reduce_totals(totals):            
        #     while True:
        #         print(f"TOTALS: {totals}")
        #         # iterate through each item in totals
        #         print(f"TOTALS KEYS:{totals.keys()}")
        #         for key in totals.keys():
        #             #if item is list of ints, reduce it to one int
        #             if not isinstance(totals[key], int) and all(isinstance(item, int) for item in totals[key]):
        #                 totals[key] = sum(totals[key])
        #             elif isinstance(totals[key], list):
        #                 values = totals[key]
        #                 print(f"current key: {values}")
        #                 for i in range(len(values)):
        #                     if isinstance(values[i], str):
        #                         print(f"in isinstance")
        #                         print(f"get: {totals.get(values[i])}")
        #                         if totals.get(values[i]) and isinstance(totals.get(values[i]), int):
        #                             values[i] = totals.get(values[i])
        #         # if all totals are ints, exit the loop and proceed to comparison
        #         if all(isinstance(totals.get(key), int) for key in totals):
        #             break
        #     print(totals)
        #     return totals

        dfs(directory)
        print(totals)

    fs = Filesystem(lines)
    fs.read_lines()
    print(f"FINAL DIRECTORY: {fs.directory}")
    count_directory_sizes(fs.directory)

find_size_of_directories_over_10000("sample_data.txt")