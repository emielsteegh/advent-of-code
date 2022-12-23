from aoc import *

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors

# A, X - Rock
# B, Y - Paper
# C, Z - Scissors


shapes = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2,
}

outcome_to_value = {
    0: 3,  # - draw,     draw
    1: 0,  # - a win,    loss
    2: 6,  # - b win,    win
}

action_to_value = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

actions = {
    'X': -1,  # lose
    'Y': 0,  # draw
    'Z': 1,  # win
}


def calc_score_1(a, b):
    score1 = shapes[a] + 1
    outcome = (shapes[a] - shapes[b]) % 3  # rps algorithm
    score1 += outcome_to_value[outcome]

    return score1


def calc_score_2(a, b):
    # for part two we figure out what needs to be played
    # r 1, p 2, s 3, index of shape_a action decides how to move in ranking
    # %3 to wrap when from 0-1 to 2 and 2+1 to 0
    score2 = [1, 2, 3][(shapes[a]+actions[b]) % 3]
    score2 += action_to_value[b]

    return score2


input = lines()
part1, part2 = 0, 0
for game in input:
    part1 += calc_score_1(game[0], game[2])
    part2 += calc_score_2(game[0], game[2])
print(part1)  # 9450
print(part2)  # 14060
