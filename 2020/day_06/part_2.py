
def count_answers():
    from string import ascii_lowercase
    with open("/Users/marce/AdventOfCode/2020/customs_answers.txt") as f:
        group_list = f.read().split("\n\n")

    answer_count = 0
    for group in group_list:
        person_list = group.split("\n")
        questions = {v:0 for k,v in enumerate(ascii_lowercase)}
        for person in person_list:
            for char in person:
                questions[char] += 1
        for value in questions.values():
            if value == len(person_list):
                answer_count += 1
    print(answer_count)