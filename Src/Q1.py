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
# K1, K2 will be affected by the environment, (i.e.) in relationship with N1, N2
# we provide the initial maximum value: K1_Init, K2_Init
# here we treat only r1 and r2 as constants
r1 = 1
r2 = 0.1
K1_Init = 50
K2_Init = 50
alpha, beta = 0.1, 0.5
sex_factor = 1
N1_init, N2_init = 10, 40 
# decay rate of K1 and K2
N1_decay = 0.02
N2_decay = 0.02
K1 = np.linspace(50,30,nNodes) + np.random.normal(0,2,nNodes)
K2 = np.linspace(30,50,nNodes) + np.random.normal(0,3,nNodes)
t = np.linspace(0,tEnd,nNodes)  # (start,stop,step)
N1 = np.zeros(nNodes)
N2 = np.zeros(nNodes)
N1[0] = N1_init
N2[0] = N2_init
# ratio of sex of lamprey
# interpolation of Rf from sample in collection of data in journal
# manual input from a sample (percent males of Lake Superior, 1946-2016) 
# from 10.1016/j.jglr.2021.09.015 and 10.1016/S0380-1330(91)71363-4
# the base is 1956
Rf_t_sample = np.array([
    1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,
    1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,
    1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,
    1984,1985,1986,1987,1995,1996,1997,1998,1999,2000,
    2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,
    2011,2012,2013,2014,2015,2016])-1954
# convert male rate to female rate
Rf_Fm_sample = 1-np.array(
    [50,58,54,57,57.5,58,59,69.5,69,70,67.2,55,52,41.5,
     33,33,27,37,30.5,30.5,30,30.5,29,30,30.3,34.5,53,
     32,33,34.3,30.9,39.1,44.1,45,56,54.2,33,34,59,42,
     47,53,54.5,56.5,57.2,54.5,53.2,66,65.8,65,62.5,61,
     54.5,63.9,51,51])/100
Rf_interp = interp1d(Rf_t_sample, Rf_Fm_sample, kind='cubic')
Rf = Rf_interp(t)
dRfdt = np.gradient(Rf, deltaT)
# nNodes-1 to prevent boundary error in N1 and N2
for i in range(nNodes):
    # for K1_tmp, we can either sample data from an article 
    # or just use a single linear decreasing model w.r.t N1 and N2
    K1_tmp = K1[i] - N1_decay * N1[i] - N2_decay * N2[i] 
    K2_tmp = K2[i] - N1_decay * N1[i] - N2_decay * N2[i] 
    #dN1 = r1 *N1[i]* (1 -(N1[i]+alpha*N2[i])/K1_tmp)
    # now sex rate is added to the model for N1(lamprey)
    dN1 = r1 *N1[i]* (1 -(N1[i]+alpha*N2[i])/K1_tmp - sex_factor*dRfdt[i])
    
    dN2 = r2 *N2[i]* (1 -(N2[i]+beta*N1[i])/K2_tmp)
    if(i != nNodes-1):
        N1[i+1] = N1[i] + dN1 * deltaT
        N2[i+1] = N2[i] + dN2 * deltaT
fig, axs = plt.subplots(3)
# set a medium size of the plot
fig.set_size_inches(15, 8)
# set a title of the plot
axs[0].set_title("1. lamprey and others competition\nr1=%.2f,r2=%.2f\nK1_Init=%.2f,K2_Init=%.2f,alpha=%.2f,beta=%.2f\n N1_decay=%.2f,N2_decay=%.2f,sex_factor=%.2f"%(r1,r2,K1_Init,K2_Init,alpha,beta,N1_decay,N2_decay,sex_factor))
axs[0].set_xlabel('time/(year)')
axs[0].set_ylabel('N/(Unit)')
axs[0].plot(t+1954, N1, label="N1(Lamprey)")
axs[0].plot(t+1954, N2, label="N2(Others)")
axs[0].legend(loc='best')
# axs[0].xlabel('t')
# plt.legend(loc='best')
# plt.show()
#axs[1].set_title("2. Sexrate of Lamprey(percentage of female) vs time")
axs[1].plot(t+1954,Rf,label="Rf")
axs[1].legend(loc='best')
axs[2].set_title("3. dRf/dt vs time")
axs[2].plot(t+1954,dRfdt,label="dRfdt")
axs[2].legend(loc='best')
plt.show()