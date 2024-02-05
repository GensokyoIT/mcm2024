import random
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time
random.seed(int(time.time()))
matplotlib.use('TKAgg')
# restrict the male reproduction times within 5 times
# male reproduction rate
mrr = [0, 1.0, 0.4107, 0.1071, 0.0714, 0.0178]

# max population of lamprey we imagine
MAX = 10000

female = [0] * (MAX + 1)
male = [0] * (MAX + 1)

# lets make gene simple
# let gene be S and s , S is dominant
# the percentage of S in population is d_rate
# we put an integer tag to describe genotype, 0 is ss, 1 is Ss or sS, and 2 is SS

d_rate = 0.5
fm_gene = [0] * (MAX + 1)
m_gene = [0] * (MAX + 1)
c_gene = [0] * (MAX + 1)
mate_list = [[] for _ in range(MAX + 1)]
child = [0] * (MAX + 1)

def give_birth(x, y):
    global c_gene,child_true
    if fm_gene[x] == 1:
        if random.random() <= 0.5:
            c_gene[x] += 1
    elif fm_gene[x] == 2:
        c_gene[x] += 1

    if m_gene[y] == 1:
        if random.random() <= 0.5:
            c_gene[x] += 1
    elif m_gene[y] == 2:
        c_gene[x] += 1

    # if child's gene >= 1 then child has S gene, then child's length is 1.0
    if c_gene[x] >= 1:
        child[x] =  1.0
        

# initialize female and male's gene and length
for i in range(1, MAX + 1):
    fm_gene[i] = m_gene[i] = 0
    for j in range(1, 3):
        fm_gene[i] += int(random.random() <= d_rate)
        m_gene[i] += int(random.random() <= d_rate)
    female[i] = int(fm_gene[i] >= 1)
    male[i] = int(m_gene[i] >= 1)

for i in range(1, MAX + 1):
    mate_count = 0
    while True:
        mate_count += 1
        if mate_count > 5:
            break
        if random.random() > mrr[mate_count]:
            break
        female_id = random.randint(1, MAX)
        mate_list[female_id].append(i)

child_count = 0
child_average = 0
new_d_rate = 0
# "clever" female strategy
# female will only accept the best male
for i in range(1, MAX + 1):
    if mate_list[i]:
        child_count += 1
        child[i] = 0
        c_gene[i] = 0
        best_male_id = mate_list[i][0]
        for m in mate_list[i]:
            if male[m] > male[best_male_id]:
                best_male_id = m
        give_birth(i, best_male_id)
        new_d_rate += c_gene[i]
        child_average += child[i]

child_average /= child_count
# new_d_rate is the sum of S gene in child S gene frequency
new_d_rate /= (child_count * 2)

print(child_count, child_average)
print(new_d_rate)
