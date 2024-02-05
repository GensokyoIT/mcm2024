import random
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats.kde import gaussian_kde
matplotlib.use('TKAgg')
# restrict the male reproduction times within 5 times
# male reproduction rate
mrr = [0, 1.0, 0.4107, 0.1071, 0.0714, 0.0178]

# max population of lamprey we imagine
MAX = 100000

female = [0] * (MAX + 1)
male = [0] * (MAX + 1)
mate_list = [[] for _ in range(MAX + 1)]
child = [0] * (MAX + 1)

random.seed(0)
eng = random.Random()
uni = random.uniform

# length of female and male
for i in range(1, MAX + 1):
    female[i] = uni(0, 1)
    male[i] = uni(0, 1)

rnd = random.Random()
# here i iterates male ID
for i in range(1, MAX + 1):
    mate_count = 0
    while True:
        mate_count += 1
        if mate_count > 5:
            break
        if uni(0, 1) > mrr[mate_count]:
            break
        female_id = rnd.randint(1, MAX)
        mate_list[female_id].append(i)

child_count = 0
child_average = 0

# "clever" female strategy
# female will only accept the best male
child_true =np.array([])
for i in range(1, MAX + 1):
    if mate_list[i]:
        child_count += 1
        child[i] = 0
        # m is i's mates' ID
        for m in mate_list[i]:
            child[i] = max(child[i], (female[i] + male[m]) / 2)
        child_average += child[i]
        #append it to child_true
        child_true = np.append(child_true, child[i])

child_average /= child_count
# create a probability vs child's length plot, using import matplot pyplot as plt lib
kde = gaussian_kde(child_true)
x_axis = np.linspace(0,1,1001)
plt.plot(x_axis, kde(x_axis))
plt.xlabel('child length')
plt.ylabel('Probability')
plt.xticks(np.arange(0, 1.0, step=0.1))

plt.axvline(x=child_average, color='b', linestyle='--')
plt.text(child_average, 0.1, 'Average=%.2f'%child_average, color='r')
plt.legend(loc='best')
plt.show()
