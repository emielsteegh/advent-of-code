from aoc import *
import itertools

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_priority(chars):
    total_priority = 0
    for ch in chars:
        total_priority += priority.index(ch)+1

    return total_priority


def calc_backpack_priority_1(content):
    # check if there is overlap between the two halves of a backpack

    h1 = set(content[:len(content)//2])
    h2 = set(content[len(content)//2:])
    intersect = h1.intersection(h2)

    return get_priority(intersect)


def calc_backpack_priority_2(*elves):
    #

    set_elves = []
    for elf in elves:
        set_elf = set(elf[:-1])
        set_elves.append(set_elf)  # remove newline and turn into set

    intersect = set_elves[0].intersection(*set_elves[1:])

    backpack_priority = 0
    for ch in intersect:
        backpack_priority += get_priority(ch)

    return backpack_priority


input = lines()

part1 = 0
part2 = 0

for line in input:
    part1 += calc_backpack_priority_1(line)
for elf1, elf2, elf3 in itertools.zip_longest(*[input]*3):
    part2 += calc_backpack_priority_2(elf1, elf2, elf3)

print(part1)  # 8515
print(part2)  # 132311
