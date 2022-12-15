
import itertools

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_priority(ch):
    return priority.index(ch)+1


def calc_backpack_priority_1(content):
    backpack_size = len(content)
    half_backpack = int(backpack_size/2) # always divisible by 2

    comp_a = set(content[:half_backpack])
    comp_b = set(content[half_backpack:])
    intersect = comp_a.intersection(comp_b)

    backpack_priority = 0
    for ch in intersect:
        backpack_priority += get_priority(ch)
    
    return backpack_priority


def calc_backpack_priority_2(*elves):
    set_elves = []
    for elf in elves:
        set_elf = set(elf[:-1])
        set_elves.append(set_elf) # remove newline and turn into set
    
    intersect = set_elves[0].intersection(*set_elves[1:])

    backpack_priority = 0
    for ch in intersect: 
        backpack_priority += get_priority(ch)
    
    return backpack_priority


INPUT_FILE = "in.txt"
if __name__ == "__main__":
    total_priority = 0
    with open(INPUT_FILE) as f:
        for line in f:
            line = line[:-1] # remove newline >:(
            total_priority += calc_backpack_priority_1(line)
    total_priority = 0
    print(total_priority)

    with open(INPUT_FILE) as f:
        for elf1,elf2,elf3 in itertools.zip_longest(*[f]*3):
            total_priority += calc_backpack_priority_2(elf1,elf2,elf3)
    print(total_priority)