from aoc import *


def find_first_unique_segment(input, seq_length):
    for line in input:
        buffer = line[:seq_length-1]
        location = 1
        for ch in range(seq_length-1, len(line)+1):
            if len(set(buffer+line[ch])) == seq_length:
                print(ch+1)
                break
            else:
                buffer = buffer[1:] + line[ch]


find_first_unique_segment(lines(), 4)  # 1356
find_first_unique_segment(lines(), 14)  # 2564
