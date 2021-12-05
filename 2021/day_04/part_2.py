"""--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

Your puzzle answer was 58838.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""

import copy


def find_final_bingo_score(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]

    # transform input into usable data
    numbers = [int(number) for number in lines[0].split(",")]
    cards = []
    new_card = []
    for i in range (2, len(lines)):
        if lines[i]:
            new_line = " ".join(lines[i].split()).split(" ")
            for j in range(0, len(new_line)):
                new_line[j] = int(new_line[j])
            new_card.append(new_line)
            if len(new_card) == 5:
                cards.append(new_card)
                new_card = []


    def mark_numbers(called_number, cards):
        # marks a number as called, then calls is_bingo to check if the called number results in a bingo
        bingo_indices = []
        for card_index in range(0, len(cards)):
            for row_index in range(0, len(cards[card_index])):
                for num_index in range(0, len(cards[card_index][row_index])):
                    if cards[card_index][row_index][num_index] == called_number:
                        cards[card_index][row_index][num_index] = str(cards[card_index][row_index][num_index])
                        if is_bingo(cards[card_index], row_index, num_index):
                            bingo_indices.append(card_index)
        return bingo_indices

    def is_bingo(card, row_index, column_index):
        # determine if a card has a vertical or horizontal bingo
        bingo_count = 0
        for number in card[row_index]:
            if type(number) == str:
                bingo_count += 1
                if bingo_count == 5:
                    return True

        bingo_count = 0
        for row in card:
            if type(row[column_index]) == str:
                bingo_count += 1
                if bingo_count == 5:
                    return True
        return False

    def card_sum(card):
        # return the sum of all non-marked numbers on a bingo card
        result = 0
        for row in card:
            for number in row:
                if type(number) == int:
                    result += number
        return result


    # run through the list of numbers, check for bingos, and store bingo data in cards_that_have_won
    cards_that_have_won = {}
    winning_order = 1

    for number in numbers:
        indeces = mark_numbers(number, cards)
        if indeces:
            for index in indeces:
                if index not in cards_that_have_won.keys():
                    winning_card = copy.deepcopy(cards[index])
                    cards_that_have_won[index] = {"winning_order": winning_order, "number": number, "winning_card": winning_card}
                    winning_order += 1

    last_winning_card_index = list(cards_that_have_won)[-1]
    last_winning_card = cards_that_have_won[last_winning_card_index]["winning_card"]
    last_bingo_number = cards_that_have_won[last_winning_card_index]["number"]
    print(f"last winning card's final score: {card_sum(last_winning_card) * last_bingo_number}")

find_final_bingo_score("data.txt")