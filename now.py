from aoc import *
from itertools import cycle  # ! looping iterators :)
from time import sleep
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Shape:
    coords: set[complex]

    def move(self, move: complex):
        coords = {c + move for c in self.coords}
        return replace(self, coords=coords)

    def can_move(self, field: set, offset: complex = (0 + 0j), x_bounds=[-1, 7]):
        for c in self.coords:
            c = c + offset
            if c.real in x_bounds:
                return False
            elif c in field:
                return False
        return True


def draw(rock, old_rock, field, height, turn, framerate=5, display_height=18):
    sleep(1 / framerate)
    print("\n" * 5)
    print(f"ROCK #{turn:05}")
    for y in range(height - 6, height + (display_height - 6)):
        print(f"y {y:05}  ", end="")
        for x in range(-1, 8):
            if x in [-1, 7]:
                print("🛢️", end="")
            else:
                c = x + y * 1j
                if c in field:
                    print("🪨", end="")
                elif c in rock.coords:
                    print("🗿", end="")
                elif c in old_rock.coords:
                    print("💨", end="")
                else:
                    print("⬜", end="")
        print(" <- H" if y == height else "")


f = lines(as_list=False).strip()
directions = {">": (1 + 0j), "<": (-1 + 0j)}
jets = cycle(enumerate([directions[t] for t in f]))
rocks = cycle(
    enumerate(
        [
            Shape({0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j}),
            Shape({0 - 1j, 1 - 1j, 2 - 1j, 1 - 2j, 1 - 0j}),
            Shape({0 + 0j, 1 + 0j, 2 + 0j, 2 - 1j, 2 - 2j}),
            Shape({0 + 0j, 0 - 1j, 0 - 2j, 0 - 3j}),
            Shape({0 + 0j, 0 - 1j, 1 + 0j, 1 - 1j}),
        ]
    )
)


def simulate(rock_count, drawing=False):
    field = set([i + 0j for i in range(7)])
    rock = Shape(set())
    max_height, i_rock, i_jet, fallen = 0, 0, 0, 0
    top_pattern = [0 for _ in range(7)]
    top_cache = {}

    while fallen < rock_count:
        if len(rock.coords) == 0:  # set next rock
            i_rock, rock = next(rocks)
            rock = rock.move(complex(2, max_height - 4))  # 2 from left, 3 from highest
        if drawing:
            old_rock = rock

        # move left/right, and test
        i_jet, jet = next(jets)
        rock = rock.move(jet) if rock.can_move(field, offset=jet) else rock

        if rock.can_move(field, offset=(1j)):
            rock = rock.move((1j))
        else:
            fallen += 1
            field.update(rock.coords)
            # calculate max y's for top pattern and max height
            for c in rock.coords:
                x, y = int(c.real), int(c.imag)
                max_height = int(min(y, max_height))  # new max y
                top_pattern[x] = min(top_pattern[x], y)  # new max y at x

            relative_top_pattern = tuple([max_height - y for y in top_pattern])
            new_top = (i_rock, i_jet, relative_top_pattern)

            # we look if this pattern has happened before so we can skip ahead
            if not new_top in top_cache:
                top_cache[new_top] = (fallen, max_height)
            else:  # we can try to skip to then end
                c_fallen, c_height = top_cache[new_top]
                # we want to fit the pattern into the remainder perfectly
                pattern_rocks = fallen - c_fallen
                pattern_height = max_height - c_height
                remaining_rocks = rock_count - fallen
                repeat, gap_to_top = divmod(remaining_rocks, pattern_rocks)

                if gap_to_top == 0:  # this pattern fits exactly until the goal
                    # instead of grabbing the first pattern, repeating it and letting it run to fallen after
                    # we find the first pattern that will repeat perfectly into fallen, no need for more sim
                    # draw(
                    #     rock=rock,
                    #     old_rock=rock,
                    #     field=field,
                    #     height=max_height,
                    #     turn=fallen,
                    #     display_height=-1 * pattern_height + 12,
                    # )
                    # print(
                    #     f"{pattern_height=}, {pattern_rocks=}, {repeat=} | {fallen=} {remaining_rocks=}"
                    # )

                    fallen += repeat * pattern_rocks
                    max_height += repeat * pattern_height
                    top_cache = {}  # reset

            rock = Shape(set())

        if drawing:
            draw(
                rock,
                old_rock,
                field,
                max_height,
                fallen,
                framerate=8,
                display_height=24,
            )

    return abs(max_height)


part1 = simulate(2022)
part2 = simulate(1e12)

print(part1)
print(part2)
