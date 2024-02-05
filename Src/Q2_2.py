import random
import time
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats.kde import gaussian_kde
matplotlib.use('TKAgg')
# restrict the male reproduction times within 5 times
# male reproduction rate
mrr = [0, 1.0, 0.4107, 0.1071, 0.0714, 0.0178]
# max population of lamprey we imagine
MAX = 10000
female = [0] * (MAX + 1)
male = [0] * (MAX + 1)
mate_list = [[] for _ in range(MAX + 1)]
child = [0] * (MAX + 1)
# Set seed using current time
random.seed(int(time.time()))
eng = random.Random()
uni = random.uniform
def check(fm, m):
    # if male's length is less and equal to half of the female's length, reject
    if m <= fm / 2:
        return False  # reject
    # if male's length is greater than 1/2 female's length, accept (probability 70% to 0%, more length more probability,
    # if male's length is at max in this case, then max probability 70%)
    # since $1\less \frac{2m}{fm}\leq 2$
    if m <= fm:
        return uni(0, 1) <= 0.7 * (m - fm / 2) / (fm / 2)  # accept
    # if male's length is greater than the female's length, accept (max probability 100%， min probability 70%)
    # more length means more probability
    if m > fm:
        return uni(0, 1) <= 0.7 + 0.3 * (m - fm) / (1.0 - fm)
# initialize a group of MAX female and male's length by random
for i in range(1, MAX + 1):
    female[i] = uni(0, 1)
    male[i] = uni(0, 1)
# here i iterates male ID
for i in range(1, MAX + 1):
    mate_count = 0
    while True:
        mate_count += 1
        if mate_count > 5:
            break
        if uni(0, 1) > mrr[mate_count]:
            break
        female_id = random.randint(1, MAX)
        mate_list[female_id].append(i)
child_count = 0
child_average = 0
child_true =np.array([])
# "probability" female strategy
# female will accept male on probability
# and the probability is influenced by the size of the male
for i in range(1, MAX + 1):
    if mate_list[i]:
        child[i] = -1
        for m in mate_list[i]:
            if not check(female[i], male[m]):
                break
            child[i] = (female[i] + male[m]) / 2
        # if child is generated, then take it into account
        if child[i] >= 0.0:
            child_count += 1
            child_average += child[i]
            #append it to child_true
            child_true = np.append(child_true, child[i])
child_average /= child_count
print("Child generated =", child_count)
print("Average length =", child_average)
kde = gaussian_kde(child_true)
x_axis = np.linspace(0,1,1001)
plt.plot(x_axis, kde(x_axis))
plt.xlabel('child length')
# x axis unit 0.1
plt.xticks(np.arange(0, 1.0, step=0.1))
plt.ylabel('Probability')
plt.legend(loc='best')
plt.axvline(x=child_average, color='b', linestyle='--')
plt.text(child_average, 0.1, 'Average=%.2f'%child_average, color='r')
plt.show()
# make a mark at x axis with label at x=0.3