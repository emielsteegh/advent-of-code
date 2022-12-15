# import
INPUTFILE = "in.txt"

def findMostCaloryElves(f_name, n):
    current_elf = 0
    elves = []
    with open(INPUTFILE) as f:
        for food in f:
            food = food[:-1]
            if not food.isnumeric():
                elves.append(current_elf)
                current_elf = 0
            else:
                current_elf += int(food)
    elves.sort()
    print(elves[-1*n:])
    return sum(elves[-1*n:])


if __name__ == "__main__":
    print(findMostCaloryElves(INPUTFILE,1))
    print(findMostCaloryElves(INPUTFILE,3))
