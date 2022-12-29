from aoc import *
from math import inf

# Today we are implementing A* once again
# Which in retro spect was total overkill
# BFS with networkx would have been much quicker to implement, but abstraction practice

def manhattan(n, n2):
    '''returns the manhattan distance between two nodes as (x,y,z) tuples'''
    if n2 == None: # in part 2 there is no single goal
        return 0
    x, y, z = n2
    dx = abs(n.x - x)
    dy = abs(n.y - y)
    dz = abs(n.z - z)
    return dx+dy+dz


def find_xy_first_match(lines, match):
    '''returns coordinates for first occurence of a character'''
    return next(
        ((line.index(match), y)
         for y, line in enumerate(lines)
         if match in line),
        None)


height = 'abcdefghijklmnopqrstuvwxyz'
def get_height(ch):
    if ch == 'S':
        ch = 'a'
    elif ch == 'E':
        ch = 'z'
    return height.index(ch)


class Node:
    __slots__ = (
        'x', 'y', 'z',
        'g', 'h', 'f',
        'parent'
    )

    def __init__(self, x, y, z, end_node_xyz):
        self.x = x
        self.y = y
        self.z = get_height(z)

        self.g = inf  # distance to start
        self.h = manhattan(self, end_node_xyz)  # estimated distance to end
        self.f = self.g + self.h
        self.parent = None

    def set_g(self, g):
        self.g = g+1
        self.f = self.g+self.h

    def set_parent(self, parent):
        self.set_g(parent.g)
        self.parent = parent

    def get_xyz(self):
        return self.x, self.y, self.z

    def get_path_len(self):
        back = self.parent
        trace = 0
        while back != None:
            back = back.parent
            trace += 1
        return(trace)

def a_star(start_node, part):
    todo = []
    done = []
    nodes = {}  # 2d array of the nodes

    end_node_xyz = None
    if part == 1:  # for part two calc end later
        end_node_xyz = (*find_xy_first_match(f, "E"), get_height("E"))

    for y, line in enumerate(f):
        for x, z in enumerate(line):
            nn = Node(x, y, z, end_node_xyz)
            nodes[(x, y)] = nn

    # find the starting point
    start_node_xy = find_xy_first_match(f, start_node)
    todo.append(start_node_xy)
    nodes[start_node_xy].g = 0

    # start a* algorithm
    while len(todo) > 0:
        todo.sort(key=lambda n: nodes[n].f, reverse=False)
        cur_xy = todo.pop(0)
        done.append(cur_xy)
        cur = nodes[cur_xy]
        x, y, z = cur.get_xyz()
        if part ==1 and cur == end_node_xyz[:2]:
            break
        elif part == 2 and cur.z == 0:
            end_node_xyz = cur.get_xyz()
            break
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nb_xy in neighbors:
            if nb_xy not in nodes.keys():
                pass  # not an existing node
            elif nb_xy in done:
                pass  # already explored
            elif(
                (part == 1 and not nodes[nb_xy].z - z <= 1) or
                # reverse route, reverse climbing
                (part == 2 and not z - nodes[nb_xy].z <= 1)
            ):
                pass
            else:
                if (nb_xy not in todo):  # not in todo
                    nodes[nb_xy].set_parent(cur)
                    todo.append(nb_xy)
                else:  # in todo
                    if (nodes[nb_xy].g > cur.g + 1):  # but worse
                        nodes[nb_xy].set_parent(cur)

    back = nodes[end_node_xyz[:2]].get_path_len()
    return back

f = lines()

print(a_star("S", part=1))  # 380
print(a_star("E", part=2))  # 375
