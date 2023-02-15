import numpy as np
import matplotlib.pyplot as plt
#quadratic trend model
def Quad(b0,b1,b2,n,ss):
    L=[]
    for t in range(n): #t=0,1,2,3,...n-1
        xt=b0+b1*t+b2*t**2+np.random.normal(0,ss**0.05)
        L.append(xt)
    return L
Q1=Quad(20,-3,0.15,100,100)

def Gr(DATA,COLOR,TITLE):
    plt.plot(DATA,color=COLOR)
    plt.title(TITLE)
    plt.show()

Gr(Q1,'r','Quad Tend')

def DIFF(DATA):
    n=len(DATA)
    L=[]
    X=DATA #X[0],X[1],...X[n-1]
    for t in range(1,n): # t=1,2,3,...,n-1
        Diff_t=X[t]-X[t-1]
        L.append(Diff_t)
    return L
DF_1=DIFF(Q1)
DF_2=DIFF(DF_1)
Gr(DF_1,'b','FirstDiff')
Gr(DF_2,'g','Second Diff')

#ARIMA(p,1,q)
def ARIMA_1(phi,th,n,ss): # ARIMA(1,1,1),ARIMA(1,1,0),ARIMA(0,1,1)
    ARMA_L=[]
    w=np.random.normal(0,ss**0.5,n+1)#w[0],w[1],...w[n]
    x0=0
    for t in range(1,n+1):#t=1,2....n
        xt=phi*x0+w[t]+th*w[t-1]
        ARMA_L.append(xt)
        x0=xt
    Delta_Y=ARMA_L
    ARIMA_L=[]
    for t in range(1,n+1):
        Yt=sum(Delta_Y[:t])
        ARIMA_L.append(Yt)
    return ARIMA_L

ARIMA_111=ARIMA_1(0.2,-0.7,400,1)
ARIMA_110=ARIMA_1(0.2,0,400,1)
ARIMA_011=ARIMA_1(0,-0.7,400,1)
Gr(ARIMA_111,'r','ARIMA(111)')
Gr(ARIMA_110,'b','ARIMA(110)')
Gr(ARIMA_011,'g','ARIMA(011)')

Dif_ARIMA_111=DIFF(ARIMA_111)
Dif_ARIMA_110=DIFF(ARIMA_110)
Dif_ARIMA_011=DIFF(ARIMA_011)
Gr(Dif_ARIMA_111,'r','D ARIMA(111)')
Gr(Dif_ARIMA_110,'b','D ARIMA(110)')
Gr(Dif_ARIMA_011,'g','D ARIMA(011)')

#ARIMA(p,2,q)
def ARIMA_2(phi, th, n, ss):
    L1 = []  # for st inv ARMA
    w = np.random.normal(0, ss ** 0.5, n + 1)
    x0 = 0
    for t in range(1, n + 1):
        xt = phi * x0 + w[t] + th * w[t - 1]
        L1.append(xt)
        x0 = xt
    Delta2_Y = L1
    L2 = []
    for t in range(1, n + 1):
        Dlt_t = sum(Delta2_Y[:t])
        L2.append(Dlt_t)
    Delta1_Y = L2
    L3 = []
    for t in range(1, n + 1):
        Yt = sum(Delta1_Y[:t])
        L3.append(Yt)
    return L3
ARIMA_121=ARIMA_2(0.2,-0.7,400,1)
ARIMA_120=ARIMA_2(0.2,0,400,1)
ARIMA_021=ARIMA_2(0,-0.7,400,1)
Gr(ARIMA_121,'r','ARIMA(121)')
Gr(ARIMA_120,'g','ARIMA(120)')
Gr(ARIMA_021,'b','ARIMA(021)')
Dif_ARIMA_121=DIFF(ARIMA_121)
Dif_ARIMA_120=DIFF(ARIMA_120)
Dif_ARIMA_021=DIFF(ARIMA_021)
Gr(Dif_ARIMA_121,'r','D ARIMA(121)')
Gr(Dif_ARIMA_120,'b','D ARIMA(120)')
Gr(Dif_ARIMA_021,'g','D ARIMA(021)')
DDif_ARIMA_121=DIFF(Dif_ARIMA_121)
DDFif_ARIMA_120=DIFF(Dif_ARIMA_120)
DDFif_ARIMA_021=DIFF(Dif_ARIMA_021)
Gr(Dif_ARIMA_121,'r','DD ARIMA(121)')
Gr(Dif_ARIMA_120,'b','DD ARIMA(120)')
Gr(Dif_ARIMA_021,'g','DD ARIMA(021)')

from statsmodels.tsa.arima.model import ARIMA

model=ARIMA(ARIMA_111,order=(1,1,1))
model_fit111=model.fit()
print(model_fit111.summary())