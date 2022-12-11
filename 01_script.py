# import
INPUTFILE = "in.txt"


def findMostCaloryElf(f_name):
    current_elf = 0
    most_calories_elf = 0
    with open(INPUTFILE) as f:
        for food in f:
            food = food[:-1]
            if not food.isnumeric():
                if current_elf > most_calories_elf:
                    most_calories_elf = current_elf
                current_elf = 0
            else:
                current_elf += int(food)
        if current_elf > most_calories_elf:
            most_calories_elf = current_elf
    return most_calories_elf

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
            # elves.append(current_elf)
    elves.sort()
    print(elves[-1*n:])
    return sum(elves[-1*n:])


if __name__ == "__main__":
    print("hi!")
    print(findMostCaloryElves(INPUTFILE,3))
    print("bye!")
