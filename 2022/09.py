import numpy as np
from aoc import *

def move(d, steps, rope, v):
    '''Moves a rope and tracks the locations it's tail end visits (v)'''
    match d:
        case 'U': d = [-1, 0]
        case 'D': d = [1, 0]
        case 'L': d = [0, -1]
        case 'R': d = [0, 1]

    for _ in range(int(steps)):
        rope[0] += d  # move head
        for seg in range(1, len(rope)):
            # difference from segment to one ahead
            delta = rope[seg-1] - rope[seg]

            if np.abs(delta).max() >= 2:  # no longer touching
                # clip to make max step in any 4-dir one
                rope[seg] += np.clip(delta, -1, 1)
                if seg == len(rope)-1:  # check if the tail end moved
                    v.add(tuple(rope[seg]))
            else:
                break  # part did not move, it's tail wont either

    return rope, v

rope1 = [np.array([0, 0]) for _ in range(2)]
rope2 = [np.array([0, 0]) for _ in range(10)]
v2 = {tuple(rope2[-1])}  # visited
v1 = {tuple(rope1[-1])}  # visited
for line in lines():
    rope1, v1 = move(*line.split(" "), rope=rope1, v=v1)
    rope2, v2 = move(*line.split(" "), rope=rope2, v=v2)
print(f"tail visited: {len(v1)}")
print(f"tail visited: {len(v2)}")
