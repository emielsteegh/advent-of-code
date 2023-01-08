from aoc import *
from itertools import product as iterproduct
from collections import defaultdict
import re


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


valves = list(rates.keys())  # all valves of intereste are the ones with flow
opened = 0  # equiv to int("0"*len(valves), 2). keeps track of opened valves
all_opened = int("1" * len(valves), 2)  # faster than recomputing


def find_max_pressure(time, cur, opened, memo=defaultdict(lambda: 0)):
    if memo[time, opened] > 0:
        return memo[time, opened]
    elif opened == all_opened:
        return 0  # no more options so we can exit
    else:
        max_pressure = 0
        for next_valve_key, next_valve_name in enumerate(valves):
            if opened & (1 << next_valve_key):  # get bit
                continue  # already opened, skip
            else:
                time_cost = dists[cur, next_valve_name] + 1
                if time_cost > time:
                    continue  # can't open this valve in time
                else:
                    next_time = time - time_cost
                    pressure_out = next_time * rates[next_valve_name]
                    next_opened = opened | (1 << next_valve_key)  # set open

                    max_pressure = max(
                        max_pressure,
                        pressure_out
                        + find_max_pressure(
                            next_time, next_valve_name, next_opened, memo
                        ),
                    )
    memo[time, opened] = max_pressure
    return max_pressure


def find_all_pressures(time, cur, opened, memo=defaultdict(lambda: 0)):
    """DP w/ memoization, slower than finding just the max pressure"""
    # loop over all valves
    for next_valve_key, next_valve_name in enumerate(valves):
        if opened & (1 << next_valve_key):  # get bit
            continue  # already opened, skip
        else:
            time_cost = dists[cur, next_valve_name] + 1
            if time_cost > time:
                # this means all plays have been made at this path, save at time=0 (end)
                memo[0, opened] = max(memo[0, opened], memo[time, opened])
            else:
                next_time = time - time_cost
                pressure_out = next_time * rates[next_valve_name]
                next_opened = opened | (1 << next_valve_key)  # set bit (open the valve)

                # update the memo
                next_pressure = max(
                    memo[next_time, next_opened], pressure_out + memo[time, opened]
                )
                memo[next_time, next_opened] = next_pressure

                if next_opened == all_opened:
                    memo[0, next_opened] = next_pressure
                else:
                    memo = find_all_pressures(
                        next_time, next_valve_name, next_opened, memo
                    )

    return memo


part1 = find_max_pressure(30, "AA", opened)


part2 = 0
pressures = find_all_pressures(26, "AA", opened)
pressures = [
    (time_open[1], pressure)
    for time_open, pressure in pressures.items()
    if time_open[0] == 0
]
pressures = sorted(pressures, key=lambda x: x[1])[-200:]

for a, b in iterproduct(pressures, pressures):
    if a[0] & b[0] == 0:
        part2 = max(part2, a[1] + b[1])

print(part2)  # 1707
print(part1)  # 2504
