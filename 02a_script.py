# A, X - Rock
# B, Y - Paper
# C, Z - Scissors


shapes = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'X' : 0,
    'Y' : 1,
    'Z' : 2,
    }

outcome_to_value = {
    0 : 3, #- draw,     draw
    1 : 0, #- a win,    loss
    2 : 6, #- b win,    win
}

def calc_score(shape_a, shape_b):
    score = shapes[shape_b] + 1
    
    outcome = (shapes[shape_a] - shapes[shape_b]) % 3
    score += outcome_to_value[outcome]
    return score

INPUTFILE = "02a_input.txt"
if __name__ == "__main__":
    total_score = 0
    with open(INPUTFILE) as f:
        for game in f:
            total_score += calc_score(game[0], game[2])
    print(total_score)