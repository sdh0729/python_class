import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Gr(D,COLOR,TITLE):
    plt.plot(D,color=COLOR)
    plt.title(TITLE)
    plt.show()

def ST(D):
    mm=np.mean(D)
    sd=np.std(D)
    X=np.array(D)
    Z=(X-mm)/sd
    print('mean=',mm,'sd=',sd)
    return Z

def CUSUM(Data): # hat T_n(t), tin[0,1]
    X=Data
    n=len(X)
    L=[]
    m=n
    Interval=np.linspace(0,1,m+1) #구간[0,1]을 m등분, 0=t0<t1<t2<...t_m=1
    for t in Interval:
        nt=int(n*t) #가우스기호
        First_Eq=sum(X[:nt])/n**0.5
        Second_Eq =t*sum(X[:nt])/n ** 0.5
        Tn_hat=First_Eq-Second_Eq
        L.append(np.abs(Tn_hat))
    print(max(L))
    return L
A=np.random.normal(0,1,100)
B=np.random.normal(5,1,100)

AA=list(A)+list(A) #200개 데이터, mean=0, sd=1
DD=list(A+list(B)) #200 change in mean from 0to5
Gr(AA,'r','AA')
Gr(DD,'b','DD')

CUS3=CUSUM(ST(AA))
CUS4=CUSUM(ST(DD))
Gr(CUS3,'r','No change in mean')
Gr(CUS4,'b','Change in mean')

def CUSUMSQ(Data):
    X=np.array(Data)
    SD=np.std(X**2)
    n=len(X)
    L=[]
    m=n
    Interval=np.linspace(0,1,m+1)
    for t in Interval:
        nt=int(n*1)
        First_Eq=sum(X[:nt])**2/n**0.5
        Second_Eq = t*sum(X[:nt]) ** 2 / n ** 0.5
        Wn_hat=First_Eq-Second_Eq
        L.append(np.abs(Wn_hat/SD))
    print(max(L))
    return L

C=np.random.normal(0,9,10)
AC=list(A)+list(C)
Gr(AC,'r','AC')
CUS8 = CUSUMSQ(AA) #No change
Gr(CUS8,'g','No change in Var')
CUS9=CUSUMSQ(AC) # change
Gr(CUS9,'b','Change in Var')
