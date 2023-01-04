from aoc import *
from itertools import product as iterproduct
from collections import defaultdict

# ! today: dynamic programming with memoization

# parsing with a nice regex tidbit
f = lines()
valves, rates, dists = set(), {}, defaultdict(lambda: 100_000)

pattern = r"Valve ([A-Z]{2}).*rate=(\d+);.* valves? (.*)"
for l in f:
    node, rate, edges = re.findall(pattern, l)[0]
    valves.add(node)
    if rate != "0":
        rates[node] = int(rate)
    for nb in edges.split(", "):
        dists[(node, nb)] = 1

# floyd-warshall for shortest path between all pairs, 2-liner
# https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
for x, a, b in iterproduct(valves, valves, valves):
    dists[a, b] = min(dists[a, b], dists[a, x] + dists[x, b])

valves = rates.keys()  # disregard the empty ones
opened = {node: False for node in valves}


def dv_to_bit(d, as_str=False):
    """converts the T/F values of the opened dict to bits"""
    s = "".join([str(int(b)) for b in d.values()])
    return s if as_str else int(s, 2)


memo = defaultdict(lambda: 0)  # stores (time, opened as int)


def find_max_pressure(time, cur, opened_dict, m=defaultdict(lambda: 0)):

    # loop over all the unopened valves
    for valve in [n for n, o in opened_dict.items() if not o]:
        opened_bit = dv_to_bit(opened_dict)

        cost = dists[cur, valve] + 1
        if cost > time:
            # this means all plays have been made at this path, save at time=0 (end)
            memo[0, opened_bit] = max(memo[0, opened_bit], memo[time, opened_bit])
            continue
        else:
            next_time = time - cost
            pressure_out = next_time * rates[valve]
            next_opened_dict = opened_dict.copy()
            next_opened_dict[valve] = True
            next_opened_bit = dv_to_bit(next_opened_dict)

            # update the memo
            next_pressure = pressure_out + memo[time, opened_bit]
            next_memo = max(memo[next_time, next_opened_bit], next_pressure)
            memo[next_time, next_opened_bit] = next_memo

            if all(next_opened_dict.values()):
                memo[0, next_opened_bit] = next_memo
            else:
                find_max_pressure(next_time, valve, next_opened_dict)


# find_max_pressure(30, 'AA', opened_dict=opened)
# get max from memo and reset ,ideally return memo
# memo = defaultdict(lambda: 0)  # stores (time, opened as int)

part2 = 0
x, y = None, None
find_max_pressure(26, "AA", opened_dict=opened)

pressures = [(time_open[1], pressure) for time_open, pressure in memo.items()]
for a, b in iterproduct(pressures, pressures):
    if a[0] & b[0] == 0:
        if a[1] + b[1] > part2:
            part2 = max(part2, a[1] + b[1])
            x, y = a, b

# print(part1)
print()
print(f"{part2}")
print(f"- {x[0]: > 08b}, {x[1]} and")
print(f"- {y[0]: > 08b}, {y[1]}")
