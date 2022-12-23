from collections import defaultdict
from itertools import accumulate
from aoc import *


sys = defaultdict(int)
curr = ['/']

for line in lines():
    # python 3.10 match case is pretty cool!
    match (line.split(' ')):
        case '$', 'cd', '/':
            curr = ['/']
        case '$', 'cd', '..':
            curr.pop()
        case '$', 'cd', directory:
            curr.append(directory+'/')
        case '$', 'ls':
            pass
        case 'dir', _:
            pass
        case size, name:
            for path in accumulate(curr):
                sys[path] += int(size)


sizes = sys.values()
part1 = sum([s for s in sizes if s <= 100_000])
minimum_delete = 30_000_000 - (70_000_000 - sys['/'])
part2 = min([s for s in sizes if s >= minimum_delete])
print(part1)  # 1423358
print(part2)  # 545729
