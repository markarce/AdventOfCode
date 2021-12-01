"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
"""

def find_occupied_seats(filename):
    with open(filename) as f: # "/Users/marce/AdventOfCode/2020/seat_layout.txt"
        seating_matrix = f.read().split("\n")

    while True:
        seats_to_flip = []
        for row_index in range(0, len(seating_matrix)):
            for seat_index in range(0, len(seating_matrix[0])):
                seat_state = seating_matrix[row_index][seat_index]
                if seat_should_flip(seat_state, row_index, seat_index, seating_matrix):
                    seats_to_flip.append((row_index, seat_index))
        if not seats_to_flip:
            break
        else:
            flip_seats(seats_to_flip, seating_matrix)
    return seating_matrix

def seat_should_flip(state, row_index, seat_index, seating_matrix):
    adjacent_seat_occupied_count = 0
    matrix_height = len(seating_matrix)
    matrix_width = len(seating_matrix[0])
    # check left if not 0
    if seat_index > 0:
        seat_to_check = seating_matrix[row_index][seat_index - 1]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    # check right if not len(row)
    if seat_index < matrix_width - 1:
        seat_to_check = seating_matrix[row_index][seat_index + 1]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    # check above if not 0
    if row_index > 0:
        seat_to_check = seating_matrix[row_index - 1][seat_index]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    # check below if not len(seating_matrix)
    if row_index < matrix_height - 1:
        seat_to_check = seating_matrix[row_index + 1][seat_index]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    # check above left
    if row_index > 0 and seat_index > 0:
        seat_to_check = seating_matrix[row_index - 1][seat_index - 1]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    # check above right
    if row_index > 0 and seat_index < matrix_width - 1:
        seat_to_check = seating_matrix[row_index - 1][seat_index + 1]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    # check below left
    if row_index < matrix_height - 1 and seat_index > 0:
        seat_to_check = seating_matrix[row_index + 1][seat_index - 1]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    # check below right
    if row_index < matrix_height - 1 and seat_index < matrix_width - 1:
        seat_to_check = seating_matrix[row_index + 1][seat_index + 1]
        if seat_to_check == "#":
            adjacent_seat_occupied_count += 1

    if state == "L" and adjacent_seat_occupied_count == 0:
        return True

    if state == "#" and adjacent_seat_occupied_count >= 4:
        return True
    else:
        return False

def flip_seats(seats_to_flip, seating_matrix):
    while len(seats_to_flip) > 0:
        seat_to_flip = seats_to_flip.pop()
        row, seat = seat_to_flip[0], seat_to_flip[1]
        target_row = seating_matrix[row]
        if target_row[seat] == "#":
            seating_matrix[row] = target_row[0:seat] + "L" + target_row[seat + 1:]
        elif target_row[seat] == "L":
            seating_matrix[row] = target_row[0:seat] + "#" + target_row[seat + 1:]
        else:
            print("shouldn't ever be here")

def count_occupied_seats(seating_matrix):
    count = 0
    for row in seating_matrix:
        for char in row:
            if char == "#":
                count += 1
    print(count)