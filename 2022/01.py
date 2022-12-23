from aoc import *


def find_most_calories(list, n_most):
    current_elf = 0
    elves = []
    for food in list:
        if not food.isnumeric():
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(food)
    elves.sort()
    return sum(elves[-1*n_most:])


input = lines()
part1, part2 = find_most_calories(input, 1), find_most_calories(input, 3)
print(part2)  # 67016
print(part2)  # 200116
