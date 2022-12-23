from aoc import *

n = numbers()
# noop lines are empty lists and just need a zero (nothing happens)
# addx lines require a zero turn before the are executed next turn
coms = [[0] + line for line in n] 
coms = [1] + [x for l in coms for x in l] # start on one and flatten
# calc pointer location at every timestep
vals = [sum(coms[:x]) for x in range(1,len(coms))]

lines = ["█" if beam%40 - vals[beam] in [-1,0,1] else " " for beam in range(0,240)]
[print("".join(lines[i-40:i])) for i in range(40,241,40)]