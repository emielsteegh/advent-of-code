from aoc import *
from itertools import product as iterproduct
from dataclasses import dataclass


@dataclass(frozen=True)
class Horizontal:
    x1: int
    x2: int
    y: int


@dataclass(frozen=True)
class Vertical:
    y1: int
    y2: int
    x: int


@dataclass(frozen=True)
class Point:
    """Immutable class that tracks x,y-points"""
    x: int
    y: int

    def __add__(self, other):
        return(Point(self.x + other.x, self.y + other.y))

    def manhattan(self, other):
        '''returns the manhattan distance between two nodes as (x,y)'''
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return dx+dy

    def rotate(self, ccw=False):
        if not ccw:
            # Rotate by 45 degrees and scale by √2
            return Point(self.x - self.y, self.x + self.y)
        else:
            # Rotate by -45 degrees and scale by √2
            return Point((self.x + self.y)/2, (self.y - self.x)/2)


def intersect(h: Horizontal, v: Vertical):
    if (v.y1 < h.y < v.y2) and (h.x1 < v.x < h.x2):  # no <= because corners are already included
        # h.y > v.y1 && h.y < v.y2
        #  h.x1 < v.x && h.x2 > v.x
        return Point(v.x, h.y)


# Parse
lines = numbers(delimiter=None)
part1_bounds, excl_part1 = [], set()
roi = 2_000_000  # row of interest
hors = set()
vers = set()
poi = set()
for x1, y1, x2, y2 in lines:
    sensor = Point(x1, y1)
    beacon = Point(x2, y2)
    reach = sensor.manhattan(beacon)

    # part 1 : a bit brutish, we check for the if the Row Of Interest is within
    # the sensor's reach, since the range is manhattan we easily caluclate what
    # part of the roi is covered by the sensor, later we join these and remove
    # the beacons on the row

    dist_to_row = abs(sensor.y - roi)
    if dist_to_row <= reach:
        width = reach-dist_to_row
        part1_bounds.append([sensor.x-width, sensor.x+width+1])
        if beacon.y == roi:
            excl_part1.add(beacon.x)

    # part 2     after some optimization considerations I decided
    # to try a python implementation of u/maneatingape's algorithm
    # https://www.reddit.com/r/adventofcode/comments/zmcn64/comment/j0d1eu8/
    # It comes down to rotating the whole thing by 45deg so we can deal with
    # straight squares and looking for the single point that is bounded by
    # four intersections (point of interests)

    tl = (sensor + Point(-reach, 0)).rotate()
    tr = (sensor + Point(0, -reach)).rotate()
    bl = (sensor + Point(0, reach)).rotate()
    br = (sensor + Point(reach, 0)).rotate()

    poi.update([tl, tr, bl, br])

    hors.add(Horizontal(tl.x, tr.x, tr.y))
    hors.add(Horizontal(bl.x, br.x, br.y))
    vers.add(Vertical(tl.y, bl.y, tl.x))
    vers.add(Vertical(tr.y, br.y, tr.x))

    # print(f"{x1},{y1},{x2},{y2}, -> {reach}")

# part 1 calculations, these are a lot faster ( O(nlogn) ) than saving the ranges
# and using itertools.chain + set operations, but also less readabale
part1_bounds.sort()
idx = 0
# find overlap of the ranges, and join them
for i in range(1, len(part1_bounds)):
    if (part1_bounds[idx][1] >= part1_bounds[i][0]):
        part1_bounds[idx][1] = max(part1_bounds[idx][1], part1_bounds[i][1])
    else:
        idx += 1
        part1_bounds[idx] = part1_bounds[i]
part1_bounds = part1_bounds[:idx+1]
# subtract the beacons in the merged ranges
part1 = 0
for bounds in part1_bounds:
    part1 += bounds[1]-bounds[0]
    for beacon in excl_part1:
        if bounds[0] <= beacon <= bounds[1]:
            part1 -= 1

# part 2
# find intersections of h and v lines, add those to poi
for (hor, ver) in iterproduct(hors, vers):
    point = intersect(hor, ver)
    if point:
        poi.add(point)

part2_gen = (
    p for p in poi if (                 # x      x 1
        (p + Point(2, 0)) in poi and    # 1 ->    P
        (p + Point(0, 2)) in poi and    # 2      2 3
        (p + Point(2, 2)) in poi        # 3
    ))

part2_point = next(part2_gen, None)
part2_point = (part2_point + Point(1, 1)).rotate(ccw=True)  # P
part2 = int(4_000_000 * (part2_point.x) + (part2_point.y))  # /2 offsets 2 * √2

# this approach could find points in overlapping sensor corners like s  <o>  s
# could be remedied by finding the next point, checking if it is within a sensor's bounds
# if so find the next, otherwise we got the one
# but there's only one point in my input anyway so no need for abstraction

print(part1)  # 6425133
print(part2)  # 10996191429555
