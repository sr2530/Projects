from collections import *
import pandas as pd

# set array of probabilities/chances for each seed
A = [0, 114, 113, 112, 111, 99, 89, 79, 69, 59, 49, 39, 29, 19, 9, 6, 4]

final_matrix = defaultdict(lambda: defaultdict(float))

# assign probability of getting 1st pick for each seed
for i in range(1, 17):
    final_matrix[i][1] = A[i] / 1000


# to find 3rd pick probability, generate all possible permutations of the previous 2 picks
def possible_2perms_draft():
    perm_list = []
    for i1 in range(1, 17):
        for i2 in range(1, 17):
            if i1 != i2:
                if (i1, i2) not in perm_list:
                    perm_list.append((i1, i2))
    return perm_list


# to find 4th pick probability, generate all possible permutations of the previous 3 picks
def possible_3perms_draft():
    perm_list = []
    for i1 in range(1, 17):
        for i2 in range(1, 17):
            for i3 in range(1, 17):
                if i1 != i2 and i1 != i3 and i2 != i3:
                    if (i1, i2, i3) not in perm_list:
                        perm_list.append((i1, i2, i3))
    return perm_list


# to find 5th pick probability, generate all possible permutations of the previous 4 picks
def possible_4perms_draft():
    perm_list = []
    for i1 in range(1, 17):
        for i2 in range(1, 17):
            for i3 in range(1, 17):
                for i4 in range(1, 17):
                    if i1 != i2 and i1 != i3 and i1 != i4 and i2 != i3 and i2 != i4 and i3 != i4:
                        if (i1, i2, i3, i4) not in perm_list:
                            perm_list.append((i1, i2, i3, i4))
    return perm_list


# to find 6th-16th pick probability, generate all possible permutations of the previous 5 picks
def possible_5perms_draft():
    perm_list = []
    for i1 in range(1, 17):
        for i2 in range(1, 17):
            for i3 in range(1, 17):
                for i4 in range(1, 17):
                    for i5 in range(1, 17):
                        if i1 != i2 and i1 != i3 and i1 != i4 and i1 != i5 and i2 != i3 and i2 != i4 and i2 != i5 \
                                and i3 != i4 and i3 != i5 and i4 != i5:
                            if (i1, i2, i3, i4, i5) not in perm_list:
                                perm_list.append((i1, i2, i3, i4, i5))
    return perm_list


print(possible_5perms_draft())


# generate 2nd pick probability for each seed
def second_pick(num_seed):
    sum = 0
    # use all possible 1st pick seeds
    for i in range(1, 17):
        if i != num_seed:
            # sum the probabilities of all scenarios with num_seed getting 2nd pick
            prob = (A[num_seed] / (1000 - A[i])) * (A[i]/1000)
            sum += prob
    return sum


# assign values in final_matrix for 2nd pick probability
for i in range(1, 17):
    prob = second_pick(i)
    final_matrix[i][2] = prob


### 3rd Pick Data
def third_pick(num_seed):
    sum = 0
    # loop over all possibilities of 1st 2 picks
    for pair in possible_2perms_draft():
        if pair[0] != num_seed and pair[1] != num_seed:
            first_pick = pair[0]
            second_pick = pair[1]
            # sum the probabilities of all scenarios with num_seed getting 3rd pick
            prob = (A[num_seed] / (1000-A[first_pick]-A[second_pick])) * (A[first_pick] / 1000) * \
                   (A[second_pick] / (1000-A[first_pick]))
            sum += prob
    return sum


# assign values in final_matrix for 3rd pick probability
for i in range(1, 17):
    prob = third_pick(i)
    final_matrix[i][3] = prob

### 4th Pick Data
#print(possible_3perms_draft())
def fourth_pick(num_seed):
    sum = 0
    # loop over all possibilities of 1st 3 picks
    for pair in possible_3perms_draft():
        if pair[0] != num_seed and pair[1] != num_seed and pair[2] != num_seed:
            first_pick = pair[0]
            second_pick = pair[1]
            third_pick = pair[2]
            # sum the probabilities of all scenarios with num_seed getting 4th pick
            prob = (A[num_seed] / (1000-A[first_pick]-A[second_pick]-A[third_pick])) * \
                   (A[first_pick] / 1000) * \
                   (A[second_pick] / (1000-A[first_pick])) * \
                   (A[third_pick] / (1000-A[first_pick]-A[second_pick]))
            sum += prob
    return sum


# assign values in final_matrix for 4th pick probability
for i in range(1, 17):
    prob = fourth_pick(i)
    final_matrix[i][4] = prob

### 5th Pick Data
def fifth_pick(num_seed):
    sum = 0
    # loop over all possibilities of 1st 4 picks
    for pair in possible_4perms_draft():
        if pair[0] != num_seed and pair[1] != num_seed and pair[2] != num_seed and pair[3] != num_seed:
            first_pick = pair[0]
            second_pick = pair[1]
            third_pick = pair[2]
            fourth_pick = pair[3]
            # sum the probabilities of all scenarios with num_seed getting 5th pick
            prob = (A[num_seed] / (1000 - A[first_pick] - A[second_pick] - A[third_pick] - A[fourth_pick])) * \
                   (A[first_pick] / 1000) * \
                   (A[second_pick] / (1000 - A[first_pick])) * \
                   (A[third_pick] / (1000 - A[first_pick] - A[second_pick])) * \
                   (A[fourth_pick] / (1000 - A[first_pick] - A[second_pick] - A[third_pick]))
            sum += prob
    return sum


# assign values in final_matrix for 5th pick probability
for i in range(1, 17):
    prob = fifth_pick(i)
    final_matrix[i][5] = prob


# picks 6-16 are pre-determined based on picks 1-5
for five_picks in possible_5perms_draft():
    picks = list(five_picks)
    first_pick = picks[0]
    second_pick = picks[1]
    third_pick = picks[2]
    fourth_pick = picks[3]
    fifth_pick = picks[4]
    # find probability of getting each 5-pick combination
    prob = (A[fifth_pick] / (1000 - A[first_pick] - A[second_pick] - A[third_pick] - A[fourth_pick])) * \
           (A[first_pick] / 1000) * \
           (A[second_pick] / (1000 - A[first_pick])) * \
           (A[third_pick] / (1000 - A[first_pick] - A[second_pick])) * \
           (A[fourth_pick] / (1000 - A[first_pick] - A[second_pick] - A[third_pick]))
    # for each 5-pick combination there is a determined order for picks 6-16
    # so add prob to the value in final_matrix at appropriate seed and pick
    for i in range(0, 12):
        for i2 in range(1, 17):
            if i2 not in picks:
                count = len(picks) + 1
                min_rank = i2
                final_matrix[min_rank][count] += prob
                picks.append(i2)

print(final_matrix)


### Checking Validity of Matrix

# sum of each row should be 1
for row in final_matrix.keys():
    print(sum(final_matrix[row].values()))

# sum of each column should also be 1
for i in range(1,17):
    sum_col = 0
    for row in final_matrix.keys():
        sum_col += final_matrix[row][i]
    print(sum_col)


# create table with appropriate columns
df = pd.DataFrame(columns=['Seed', 'Chances', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
df['Seed'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
A_copy = A
A_copy.pop(0)
df['Chances'] = A_copy
# set probabilities in the table using final_matrix
for seed in range(16):
    for pick in range(1, 17):
        df.loc[seed, pick] = round(final_matrix[seed+1][pick], 4)
# rename columns to proper format
df.columns = ['Seed', 'Chances', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th',
              '12th', '13th', '14th', '15th', '16th']

print(df)
df.to_csv('DraftProbabilityTable.csv', index=False)

