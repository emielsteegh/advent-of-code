from aoc import *
from time import sleep

# ! trying out complex numbers for coordinates


f = lines()
blocked = set()  # tracks coords with blocked spaces
low = 0

# parse playing field (rocks)
for line in f:
    line = [[int(i) for i in c.split(",")] for c in line.split(" -> ")]
    pairs = zip(line, line[1:])
    for (x1, y1), (x2, y2) in pairs:
        low = max(y1, y2, low)

        for x in range(min(x1, x2), max(x1, x2)+1):
            for y in range(min(y1, y2), max(y1, y2)+1):
                # ! real numbers caputre x, complex numbers y
                blocked.add(x + y*1j)

spawn = (500 + 0j)

# set floor at lowest rock +2
floor = low+2
# technically infinite, but wont get bigger than a triangle from the spawn
floor_x_range = range(int(spawn.real)-floor-1, int(spawn.real)+floor+2)
blocked.update([(x + floor * 1j) for x in floor_x_range])


sc, part1, part2 = 0, None, None  # sand counter
simulating = True
while simulating:
    sc += 1
    sand = spawn
    while "falling":  # nice to read but takes longer to eval than True ?
        if (sand + 1j) not in blocked:  # down
            sand += 1j
        elif (sand + -1+1j) not in blocked:  # down right
            sand += -1+1j
        elif (sand + 1+1j) not in blocked:  # down left
            sand += 1+1j
        else:  # stopped
            blocked.add(sand)
            if sand == spawn:  # at spawn, part 2 finished
                part2 = sc
                simulating = False
                break
            break

        if part1 == None and sand.imag > low:  # part 1 finished
            part1 = sc-1  # current is the first that fell off, were looking for last to stay


print(part1)  # 625
print(part2)  # 25193
