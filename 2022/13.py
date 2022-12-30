from aoc import *
import ast
from math import prod
from copy import deepcopy


def get_next(lst):
    nxt, rest = None, None
    if len(lst) > 0:
        nxt = lst.pop(0)
        rest = lst
    return nxt, rest


def compare(l, r, d):
    il, l = get_next(l)
    ir, r = get_next(r)

    match il, ir:
        case None, None:  # end of a list
            return None
        case int(), list():  # one is not a list, make it such
            il = [il]
        case list(), int():
            ir = [ir]

    match il, ir:
        case list(), list():  # go deeper
            sub_lists = compare(il, ir, d+1)
            if sub_lists is not None:
                return sub_lists
        case int(), int():  # compare
            if il != ir:
                return il < ir
        case None, _:
            return True
        case _, None:
            return False

    return compare(l, r, d)


def replace_empty_then_flat(l, r):
    '''replaces empty lists with [r] and flattens the list'''
    s = str(l).replace("[]", f"[{r}]")
    l = string_to_numbers(s, delimiter=None)
    return l


# ! read input
pairs = lines(as_list=False).split('\n\n')
pairs = [[ast.literal_eval(p) for p in pair.split('\n') if p]
         for pair in pairs]

# ! part 1: recursive dequeing lists while following the ruleset
part1 = []
for i, pair in enumerate(pairs):
    l, r = deepcopy(pair)
    pair_in_order = compare(l, r, 0)
    if pair_in_order:
        part1.append(i+1)


# ! part 2: for sorting the whole nested list business does not matter, get rid of it
numbers = [replace_empty_then_flat(p, -1) for pair in pairs for p in pair]
decoders = [[2], [6]]
numbers.extend(decoders)
numbers = sorted(numbers)
part2 = [numbers.index(d)+1 for d in decoders]

print(sum(part1))  # 6070
print(prod(part2))  # 20758
