"""
Secret Santa
For each couple (A, B, C, ...), we want to create a selection of two other people 
that they will have to get presents to. The couples buy presents together, but 
they can get random people to give presents to. 

Each couple gets an individual file that can be sent to them annonymously.

The constraints of this problem are:
 - The couples cannot get themselves
 - Each person can only be selected once
 
 Currently, the code is run multiple times until the constraints are made. 

"""
import numpy as np

individuals = [ 'A1', 'A2',
                'B1', 'B2',
                'C1', 'C2',
                'D1', 'D2',
                'E1', 'E2',
                'F1', 'F2', 
                'G1', 'G2']

# Create couples
couples = list()
for i in range(len(individuals)//2):
    couples.append(individuals[2*i:2*i+2])

# Create constraints
# 1. Couples cannot get themselves
def find_indexes_nonrepeat(couples, individuals):
    terminated = False    
    random_index = np.arange(0, len(individuals))
    while terminated == False:
        np.random.shuffle(random_index)
        list_match = np.zeros(len(individuals))
        for i in range(len(couples)):
            if individuals[random_index[2*i]] in couples[i]:
                list_match[2*i] = 1
            if individuals[random_index[2*i+1]] in couples[i]:
                list_match[2*i+1] = 1

        if np.count_nonzero(list_match) == 0: 
            return random_index

indexes = find_indexes_nonrepeat(couples, individuals)

# Assign to couples
couple_goals = list()
for i in range(len(couples)):
    couple_goals.append([individuals[indexes[2*i]], individuals[indexes[2*i+1]]])
    with open('./couple_%i'%i +'.txt', 'w') as f:
        f.write('%s, %s'%(couple_goals[i][0], couple_goals[i][1]))
# print(couple_goals)

