from aoc import *
import re


full_overlap_pairs = 0
overlap_pairs = 0

for pair in lines():
    elf1a, elf1b, elf2a, elf2b = [int(x) for x in re.split('[,-]', pair)]

    elf1 = set(range(elf1a, elf1b+1))
    elf2 = set(range(elf2a, elf2b+1))

    if (elf1.issubset(elf2) or elf2.issubset(elf1)):
        full_overlap_pairs += 1

    if elf1.intersection(elf2):
        overlap_pairs += 1

print(full_overlap_pairs)  # 582
print(overlap_pairs)      # 893
