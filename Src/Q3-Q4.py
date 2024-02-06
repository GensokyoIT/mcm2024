# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
from numpy import mat
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
trans = np.array( [[0.78,0.1 ,0.1 ,0.0 ,0.1 ,0.0 ],
				   [0.0 ,0.82,0.15,0.0 ,0.1 ,0.2 ],
				   [0.0 ,0.0 ,0.82,0.18,0.18,0.0 ],
				   [0.0 ,0.2 ,0.0 ,0.82,0.18,0.0 ],
				   [0.0 ,0.18,0.0 ,0.0 ,0.82,0.25],
				   [0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,2.72]] )
# non divergent
# trans = np.array( [[0.78,0.1 ,0.1 ,0.0 ,0.1 ,0.0 ],
# 				   [0.0 ,0.82,0.15,0.0 ,0.1 ,0 ],
# 				   [0.0 ,0.0 ,0.82,0.18,0.18,0.0 ],
# 				   [0.0 ,0 ,0.0 ,0.82,0.18,0.0 ],
# 				   [0.0 ,0,0.0 ,0.0 ,0.82,0.25],
# 				   [0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,2.72]] )
popu = np.array( [0.11,0.28,0.10,0.17,0.37,1.00] )
popu1= np.zeros( (6) )

x_axis = np.linspace(0,300,300)
print(trans)
# population by year
pby  = np.zeros( (1000,6) )

for i in range(0,6):
	pby[0][i] = popu[i]

for gen in range(1,1000):
	popu1 = np.zeros( (6) )
	for i in range(0,6):
		for j in range(0,6):
			popu1[i] += popu[j] * trans[i][j]
			popu1[i] -= popu[j] * trans[j][i] * 0.6
	if( popu1[5] > 1.20 ):
		trans[5][5] -= 0.02
	if( popu1[5] < 0.83 ):
		trans[5][5] += 0.02
	for i in range(0,6):
		pby[gen][i] = popu[i] = popu1[i]
# get pby by column
fig, axs = plt.subplots(2)
# set a medium size of the plot
fig.set_size_inches(15, 8)
# set a title of the plot
#axs[0].set_title('Population by year')
axs[0].set_xlabel('time/(year)')
axs[0].set_ylabel('N/(Unit)')
axs[0].plot(x_axis, pby[300:600,0], label="N0(Parasite)")
axs[0].plot(x_axis, pby[300:600,1], label="N1(Lamprey)")
axs[0].plot(x_axis, pby[300:600,2], label="N2(big meat-eating fish)")
axs[0].plot(x_axis, pby[300:600,3], label="N3(Small meat-eating fish)")
axs[0].plot(x_axis, pby[300:600,4], label="N4(Seaweed-eating fish)")
axs[0].plot(x_axis, pby[300:600,5], label="N5(Seaweed)")
axs[0].legend(loc='best')
plt.show()