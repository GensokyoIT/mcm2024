from scipy.integrate import odeint  # 导入 scipy.integrate 模块
import numpy as np  # 导入 numpy包
import matplotlib
import matplotlib.pyplot as plt  # 导入 matplotlib包
# 别用Qt5, my conda env is not compatible with it
matplotlib.use('TKAgg')
# 设置模型参数
tEnd = 300  # 预测长度
nNodes = 100000 #采样点数
deltaT = tEnd / nNodes  # 采样间隔
# brief: 
# here number #1 means Lamprey, #2 means others
# alpha is 2 to 1, that is impact of others on lamprey
# beta is 1 to 2, that is impact of lamprey on others
#
# K1, K2 will be affected by the environment, (i.e.) in relationship with N1, N2
# we provide the initial maximum value: K1_Init, K2_Init
# here we treat only r1 and r2 as constants
r1 = 1
r2 = 0.1
K1_Init = 50
K2_Init = 50
alpha, beta = 0.1, 0.5
# 初值
N1_init, N2_init = 10, 10  
# decay rate of K1 and K2
K1_decay = 0
K2_decay = 0

t = np.linspace(0,tEnd,nNodes)  # (start,stop,step)
N1 = np.zeros(nNodes)
N2 = np.zeros(nNodes)
# ratio of sex of lamprey
Rf = np.zeros(nNodes)
N1[0] = N1_init
N2[0] = N2_init

#TODO interpolation of Rf from sample in collection of data in journal
# Rf = interp1d(x, y, kind='cubic')

# nNodes-1 to prevent boundary error in N1 and N2
for i in range(nNodes):
    # for K1_tmp, we can either sample data from an article 
    # or just use a single linear decreasing model w.r.t N1 and N2
    K1_tmp = K1_Init - K1_decay * N1[i]
    K2_tmp = K2_Init - K2_decay * N2[i]
    dN1 = r1 *N1[i]* (1 -(N1[i]+alpha*N2[i])/K1_tmp)
    dN2 = r2 *N2[i]* (1 -(N2[i]+beta*N1[i])/K2_tmp)
    if(i != nNodes-1):
        N1[i+1] = N1[i] + dN1 * deltaT
        N2[i+1] = N2[i] + dN2 * deltaT
#
plt.figure(figsize=(9,9))
# set a title of the plot
plt.title("1. lamprey and others competition\nr1=%.2f,r2=%.2f\nK1_Init=%.2f,K2_Init=%.2f,alpha=%.2f,beta=%.2f\n K1_decay=%.2f,K1_decay=%.2f"%(r1,r2,K1_Init,K2_Init,alpha,beta,K1_decay,K2_decay))
# plt.subplot(121), 
plt.plot(t, N1, label="N1(Lamprey)")
plt.plot(t, N2, label="N2(Others)")
plt.xlabel('t')
plt.legend(loc='best')
plt.show()