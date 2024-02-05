import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
import numpy as np
import matplotlib.pyplot as plt

# Energy needed by a single fish
for i in range(6):
    for j in range (6):
        print("A_{%d%d} &"%(i+1,j+1),end="")
    print("\\\\")
x = np.linspace(0,20,101)
y= 0.12+x
# Set labels and title
plt.plot(x,y)
plt.xlabel('PERCENT FEMALES')
plt.ylabel('Energy needed')
# disable display of y range
# turn off y axes 

plt.ylim(0,1.2)
plt.yticks([])
plt.xlim(0,1)
# Show the plot
#plt.show()
