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

#Gr(Q1,'r','Quad Tend')

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
#Gr(DF_1,'b','FirstDiff')
#Gr(DF_2,'g','Second Diff')

#ARIMA(p,1,q)
def ARIMA_212(phi1,phi2,th1,th2,n,ss):
    ARMA_L=[]
    w=np.random.normal(0,ss**0.5,n+2)
    x0=0
    x00=0
    for t in range(2,n+2):#t=1,2....n
        xt=phi1*x0+phi2*x00+w[t]+th1*w[t-1]+th2*w[t-2]
        ARMA_L.append(xt)
        x00 = x0
        x0=xt
    Delta_Y=ARMA_L
    ARIMA_L=[]
    for t in range(2,n+2):
        Yt=sum(Delta_Y[:t])
        ARIMA_L.append(Yt)
    return ARIMA_L
ARIMA_212=ARIMA_212(0.2,-0.7,0.5,0.3,400,1)
Gr(ARIMA_212,'r','ARIMA(212)')
Dif_ARIMA_212=DIFF(ARIMA_212)
Gr(Dif_ARIMA_212,'r','D ARIMA(212)')

from statsmodels.tsa.arima.model import ARIMA

model=ARIMA(Dif_ARIMA_212, order=(2,1,2))
modelfit_212=model.fit
print(modelfit_212.summary())

