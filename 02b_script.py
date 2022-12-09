# A, X - Rock
# B, Y - Paper
# C, Z - Scissors


shapes = {
    'A' : 0, #
    'B' : 1, #
    'C' : 2, # used as shape index
    }
    
actions = {
    'X' : -1,  # lose
    'Y' : 0,  # draw 
    'Z' : 1, # win
    }

action_to_value = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6,
}


def calc_score(shape_a, action):
    # r 1, p 2, s 3, index of shape_a action decides how to move in ranking
    score = [1,2,3][(shapes[shape_a]+actions[action])%3] # %3 to wrap when from 0-1 to 2 and 2+1 to 0
    score += action_to_value[action]
    return score

INPUTFILE = "02_input.txt"
if __name__ == "__main__":
    total_score = 0
    with open(INPUTFILE) as file:
        for game in file:
            total_score += calc_score(game[0], game[2])
    print(total_score)
