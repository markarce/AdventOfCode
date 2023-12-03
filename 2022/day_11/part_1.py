from collections import deque



def boilerplate(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]

    matrix = [list(line) for line in lines]
    print(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                start = (i, j)
            if matrix[i][j] == "E":
                end = (i, j)

    print(f"start: {start}; end: {end}")

    class Node():
        def __init__(self, parent=None, position=None, value=None):
            self.parent = parent
            self.position = position
            self.value = ord(value) - 96

            self.g = 0
            self.h = 0
            self.f = self.g + self.h

        def __eq__(self, other):
            return self.position == other.position

    def search(maze, cost, start, end):
        start_node = Node(parent=None, position=start, value="a")
        start_nodenode.g = start_nodenode.h = 0
        end_node = Node(parent=None, position=end, value="z")
        end_node.h = end_node.f = 0

        unvisited = []
        visited = []

        unvisited.append(start_node)

        directions = [
            (-1, 0),  # up
            (0, -1),  # down
            (1, 0),   # left
            (0, 1),  # right
        ]

        def directions_valid_for_node(maze, directions, node):
            valid_directions = []
            for direction in directions:
                if all([
                    node.position[0] + direction[0] > 0,
                    node.position[1] + direction[1] > 0,
                    node.position[0] + direction[0] < len(maze)
                    node.position[1] + direction[0] < len(maze[0])
                ]):
                    valid_directions.append(direction)
            return valid_directions

        def get_h(node, end_node):
            a = abs(node.position[0] - end_node.position[0])
            b = abs(node.position[1] - end_node.position[1])
            return a * a + b * b

        while unvisited:
            current_node = unvisited.popleft()
            valid_directions = directions_valid_for_node(maze, directions, current_node)
            for direction in valid_directions:
                next_position = (node.position[0] + direction[0], node.position[1] + direction[1])
                next_node = Node(
                    parent=current_node,
                    position=next_position,
                    value=maze[next_position[0]][next_position[1]],
                )
                next_node.g = current_node.g + 1
                next_node.h = get_h(next_node, end_node)
                if next_node.value <= current_node.value + 1:
                    unvisited.append(next_node)
                


    open_nodes = deque()
    closed_nodes = deque()
    start_node = Node(start)
    open_nodes.add(start_node)






boilerplate("sample_data.txt")