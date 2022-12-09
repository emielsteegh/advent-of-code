import re

INPUT_FILE = "04_input.txt"
if __name__ == "__main__":
    full_overlap_pairs = 0
    overlap_pairs = 0
    with open(INPUT_FILE) as file:
        for pair in file:
            pair=pair[:-1]
            elf1a, elf1b, elf2a, elf2b = [int(x) for x in re.split('[,-]', pair)]

            elf1 = set(range(elf1a,elf1b+1))
            elf2 = set(range(elf2a,elf2b+1))

            # if (
            #     ((elf1a<=elf2a<=elf1b) and (elf1a<=elf2b<=elf1b))
            #     or
            #     ((elf2a<=elf1a<=elf2b) and (elf2a<=elf1b<=elf2b))
            # ):
            #     overlap_pairs += 1
            
            if (elf1.issubset(elf2) or elf2.issubset(elf1)):
                full_overlap_pairs += 1
            
            if elf1.intersection(elf2):
                overlap_pairs += 1

    print(full_overlap_pairs)
    print(overlap_pairs)