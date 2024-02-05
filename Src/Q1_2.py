from scipy.interpolate import interp1d
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt  
matplotlib.use('TKAgg')
tEnd = 2016-1954  
nNodes = 100000 
deltaT = tEnd / nNodes  
# brief: 
# here number #1 means Lamprey, #2 means others
# alpha is 2 to 1, that is impact of others on lamprey
# beta is 1 to 2, that is impact of lamprey on others
#
# K1, K2 will be affected by the environment, (i.e.) in relationship with N1, N0
# we provide the initial maximum value: K1_Init, K2_Init
# here we treat only r1 and r2 as constants
r = 0.5
alpha, beta = 2, 0.3
delta = 0.05
# 初值
N1_init, N0_init = 10, 40 
sex_factor = 0

t = np.linspace(0,tEnd,nNodes)  # (start,stop,step)
N1 = np.zeros(nNodes)
N0 = np.zeros(nNodes)
# ratio of sex of lamprey
Rf = np.zeros(nNodes)
N1[0] = N1_init
N0[0] = N0_init

# interpolation of Rf from sample in collection of data in journal
# manual input from a sample (percent males of Lake Superior, 1946-2016) 
# from 10.1016/j.jglr.2021.09.015 and 10.1016/S0380-1330(91)71363-4
# the base is 1956
Rf_t_sample = np.array([1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])-1954
# convert male rate to female rate
Rf_Fm_sample = 1-np.array([50,58,54,57,57.5,58,59,69.5,69,70,67.2,55,52,41.5,33,33,27,37,30.5,30.5,30,30.5,29,30,30.3,34.5,53,32,33,34.3,30.9,39.1,44.1,45,56,54.2,33,34,59,42,47,53,54.5,56.5,57.2,54.5,53.2,66,65.8,65,62.5,61,54.5,63.9,51,51])/100

Rf_interp = interp1d(Rf_t_sample, Rf_Fm_sample, kind='cubic')
Rf = Rf_interp(t)
dRfdt = np.gradient(Rf, deltaT)
# nNodes-1 to prevent boundary error in N1 and N0
for i in range(nNodes):
    # for K1_tmp, we can either sample data from an article 
    # or just use a single linear decreasing model w.r.t N1 and N0
    
    #dN1 = r1 *N1[i]* (1 -(N1[i]+alpha*N0[i])/K1_tmp)
    # now sex rate is added to the model for N1(lamprey)
    dN0 = alpha*N0[i] - beta*N0[i]*N1[i]
    dN1 = delta*N0[i]*N1[i] -r*N1[i] -sex_factor*abs(dRfdt[i])*N1[i]
    if(i != nNodes-1):
        N1[i+1] = N1[i] + dN1 * deltaT
        N0[i+1] = N0[i] + dN0 * deltaT
#
fig, axs = plt.subplots(3)
# set a medium size of the plot
fig.set_size_inches(15, 8)
# set a title of the plot
axs[0].set_title("Q3. lamprey and prey\nalpha=%.2f,beta=%.2f,delta=%.2f,r=%.2f,sex_factor=%.2f"%(alpha,beta,delta,r,sex_factor))
axs[0].set_xlabel('t')
axs[0].plot(t+1954, N1, label="N1(Lamprey)")
axs[0].plot(t+1954, N0, label="N0(prey)")
axs[0].legend(loc='best')
axs[0].set_xlabel('t')
axs[0].set_ylabel('N')

axs[1].set_title("2. Sexrate of Lamprey(percentage of female) vs time")
axs[1].plot(t+1954,Rf,label="Rf")
axs[1].legend(loc='best')

axs[2].set_title("3. dRf/dt vs time")
axs[2].plot(t+1954,dRfdt,label="dRfdt")
axs[2].legend(loc='best')
plt.show()