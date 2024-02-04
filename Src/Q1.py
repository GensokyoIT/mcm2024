from scipy.integrate import odeint  # 导入 scipy.integrate 模块
import numpy as np  # 导入 numpy包
import matplotlib
import matplotlib.pyplot as plt  # 导入 matplotlib包
matplotlib.use('TKAgg')
# here number #1 means Lamprey, #2 means others
r1 = 1
r2 = 0.1
K1 = 50
K2 = 50

def dyComptition(vars, t, alpha, beta):  # 2物种LK模型，导数函数
    # import global constants
    global r1,r2
    # here N1 is lamprey, N2 is others
    N1, N2 = vars
    # alpha, beta = args
    dN1 = r1 * (1 -(N1+alpha*N2)/K1)
    dN2 = r2 * (1 -(N2+beta*N1)/K2)
    # odeint solver requires an array of derivatives as return value
    return np.array([dN1, dN2])

# 设置模型参数
# alpha is 2 to 1, that is impact of others on lamprey
# beta is 1 to 2, that is impact of lamprey on others
alfa, beta = 0.1, 0.5
tEnd = 1000  # 预测长度
t = np.arange(0.0, tEnd, 0.01)  # (start,stop,step)
# 初值
N1_init, N2_init = 10, 10  
Y0 = (N1_init, N2_init) 

plt.figure(figsize=(9,6))
# set a title of the plot
plt.title("1. lamprey and others competition\nr1=%.2f,r2=%.2f,K1=%.2f,K2=%.2f,alpha=%.2f,beta=%.2f"%(r1,r2,K1,K2,alfa,beta))
# plt.subplot(121), 
yt = odeint(dyComptition, Y0, t, args=(alfa, beta))  # SIS 模型
plt.plot(t, yt[:,0], label="N1(Lamprey)")
plt.plot(t, yt[:,1], label="N2(Others)")
plt.xlabel('t')
plt.legend(loc='best')
plt.show()