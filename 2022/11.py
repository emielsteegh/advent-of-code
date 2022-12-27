from aoc import *
from collections import defaultdict
from operator import mul, add
from copy import deepcopy
from math import lcm
f = lines(as_list=False).split('\n\n')


class Monkey:
    __slots__ = (
        'items',
        'op', 'op_val',
        'test_div', 'if_true', 'if_false',
        'inspects'
    )

    def __init__(self, blueprint):
        lines = blueprint.split('\n')
        # self.id = string_to_numbers(lines[0])[0]
        self.items = string_to_numbers(lines[1], ',')
        operation = lines[2].split(' ')
        self.op = mul if operation[-2] == '*' else add
        self.op_val = operation[-1]
        self.test_div = string_to_numbers(lines[3])[0]
        self.if_true = string_to_numbers(lines[4])[0]
        self.if_false = string_to_numbers(lines[5])[0]
        self.inspects = 0

    def inspect(self):
        self.inspects += 1
        pass_to = None

        item = self.items.pop()  # take item
        # can be "old", in that case use item value
        op_val = int(self.op_val) if self.op_val != 'old' else item
        item = self.op(item, op_val)  # increase value

        return item


def play(monkeys, rounds, part):
    for r in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.inspect()
                if part == 1:
                    item //= 3
                if part == 2:
                    item %= monkey_lcm  # ! keep values small to prevent overflow
                pass_to = monkey.if_true if item % monkey.test_div == 0 else monkey.if_false
                monkeys[pass_to].items.append(item)
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspects)
    inspections = sorted(inspections)
    print(inspections[-1] * inspections[-2])


# init
monkeys = []
test_values = []
for monkey_blueprint in f:
    new_monkey = Monkey(monkey_blueprint)
    monkeys.append(new_monkey)
    test_values.append(new_monkey.test_div)
# ! using a value that retains congruency between test_div's
monkey_lcm = lcm(*test_values)

monkeys_2 = deepcopy(monkeys)

play(monkeys, 20, part=1)  # 151312
play(monkeys_2, 10_000, part=2)  # 51382025916
