
import itertools

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_priority(ch):
    return priority.index(ch)+1

def calc_backpack_priority(*elves):
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
    with open(INPUT_FILE) as file:
        for elf1,elf2,elf3 in itertools.zip_longest(*[file]*3):
            total_priority += calc_backpack_priority(elf1,elf2,elf3)
    print(total_priority)