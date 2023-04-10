import array

def display_grid(VankinsGrid):
    for r in range(len(VankinsGrid)):
        for c in range(len(VankinsGrid[0])):
            print(str(VankinsGrid[r][c]), end = "\t")
        print("")

def evalunit(VankinsGrid, r = 0, c = 0):
    unitscore = VankinsGrid[r][c]
    upscore = 0
    leftscore = 0
    if(r < len(VankinsGrid) - 1):
        upscore = evalunit(VankinsGrid, r + 1, c)
    if(c < len(VankinsGrid[0]) - 1):
        leftscore = evalunit(VankinsGrid, r, c + 1)
    return max(upscore + unitscore, leftscore + unitscore)

def evalunitMin(VankinsGrid, r = 0, c = 0):
    unitscore = VankinsGrid[r][c]
    upscore = 0
    leftscore = 0
    if(r < len(VankinsGrid) - 1):
        upscore = evalunitMin(VankinsGrid, r + 1, c)
    if(c < len(VankinsGrid[0]) - 1):
        leftscore = evalunitMin(VankinsGrid, r, c + 1)
    return min(upscore + unitscore, leftscore + unitscore)


test = [[6,-2,-5,7,-4],
[-4,-6,3,-4,-5],
[4,-3,5,-1,3],
[-4,6,-3,4,2],
[5,-1,6,-1,-7]]

print("Welcome to Vankins Mile")
display_grid(test)
score = evalunit(test)
score2 = evalunitMin(test)
print("The maximum score possible on this grid is " + str(score))
print("The minimum score possible on this grid is " + str(score2))

import random

def generate_branch_sequence(difficulty, sequence_length):
    if difficulty == "easy":
        min_spacing = 4
    elif difficulty == "medium":
        min_spacing = 3
    elif difficulty == "difficult":
        min_spacing = 2
    else:
        raise ValueError("Invalid difficulty level")

    branch_sequence = []
    current_pos = random.randint(4, 12)
    while len(branch_sequence) < sequence_length:
        branch_spacing = random.randint(min_spacing, 8)
        next_pos = (current_pos + branch_spacing) % 16
        if next_pos >= current_pos:
            branch_length = 3
        else:
            branch_length = 3 - (current_pos - next_pos)
        for i in range(8):
            if i == current_pos or i == current_pos + 1 or i == current_pos + 2:
                branch_sequence.append([i, branch_length])
            else:
                branch_sequence.append([i, 0])
        current_pos = next_pos
    return branch_sequence

easy_sequence = generate_branch_sequence("easy", 100)
medium_sequence = generate_branch_sequence("medium", 100)
difficult_sequence = generate_branch_sequence("difficult", 100)
print (easy_sequence)