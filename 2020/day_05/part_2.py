def read_boarding_passes():
    with open("/Users/marce/AdventOfCode/2020/Boarding.txt") as f:
        boarding_passes = f.read().split("\n")
    seat_ids = []
    for boarding_pass in boarding_passes:
        row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
        column = int(boarding_pass[-3:].replace("L", "0").replace("R", "1"), 2)
        seat_id = 8 * row + column
        seat_ids.append(seat_id)
    seat_ids.sort()
    for seat in range(len(seat_ids)):
        if seat_ids[seat + 1] != seat_ids[seat] + 1:
            return seat_ids[seat] + 1