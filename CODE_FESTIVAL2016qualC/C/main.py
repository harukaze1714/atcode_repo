K,T=map(int,input().split())
N=list(map(int,input().split()))

L=[[i for i in range(2)]for j in range(T)]
for i in range(T):
    L[i][0]=i
    L[i][1]=N[i]

f=-1
c=0
for K in range(K):    
    L1=sorted(L,key=lambda x:x[1])
    if(f!=L1[-1][0]):
        f=L1[-1][0]
        L1[-1][1]-=1
    elif(L1[T-2][1]>0 and L1[T-2][0]!=f):
        f=L1[T-2][0]
        L1[T-2][1]-=1     
    else:
        c+=1
        f=L1[-1][0]
        L1[-1][1]-=1       
print(c)    