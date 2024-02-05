# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import numpy as np
from numpy import mat
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TKAgg')
trans = np.array( [[0.78,0.1 ,0.1 ,0.0 ,0.1 ,0.0 ],
				   [0.0 ,0.82,0.15,0.0 ,0.1 ,0.08],
				   [0.0 ,0.0 ,0.82,0.18,0.18,0.0 ],
				   [0.0 ,0.1 ,0.0 ,0.82,0.18,0.0 ],
				   [0.0 ,0.08,0.0 ,0.0 ,0.82,0.25],
				   [0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,1.15]] )

popu = np.array( [1.0,1.0,1.0,1.0,1.5,2.0] )
popu1= np.zeros( (6) )

# population by year
pby  = np.zeros( (1000,6) )
x_axis = np.linspace(20,199,180)
for i in range(0,6):
	pby[0][i] = popu[i]

for gen in range(0,1000):
	popu1 = np.zeros( (6) )
	for i in range(0,6):
		popu1[i] = popu[i] * trans[i][i]
		for j in range(0,6):
			if( i != j ):
				popu1[i] += popu[i] * popu[j] * trans[i][j]
				popu1[i] -= popu[i] * popu[j] * trans[j][i] * 0.6
	            
	for i in range(0,6):
		popu1[i] = min( popu1[i] , 1.5 + 0.5 * max( 0 , i - 3 ) )
		popu1[i] = max( popu1[i] , 0.1 )
		pby[gen][i] = popu[i] = popu1[i]

# get pby by column
fig, axs = plt.subplots(2)
# set a medium size of the plot
fig.set_size_inches(15, 8)
# set a title of the plot
axs[0].set_title('Population by year')
axs[0].set_xlabel('t')
axs[0].plot(x_axis, pby[20:200,0], label="N0(Parasite)")
axs[0].plot(x_axis, pby[20:200,1], label="N1(Lamprey)")
axs[0].plot(x_axis, pby[20:200,2], label="N2(big meat-eating fish)")
axs[0].plot(x_axis, pby[20:200,3], label="N3(Small meat-eating fish)")
axs[0].plot(x_axis, pby[20:200,4], label="N4(Seaweed-eating fish)")
axs[0].plot(x_axis, pby[20:200,5], label="N5(Seaweed)")
axs[0].legend(loc='best')
plt.show()