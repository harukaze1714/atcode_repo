N = int(input())
A=[0]*N
P=[0]*N


for i in range(N):
    A[i] = list(map(int,input().split()))
for i in range(N):
    P[i] = list(map(int,input().split()))

MAX=-1*(10**9)
for i in range(1,1024):
    t=format(i,"b")
    l=10-len(t)
    t="0"*l+t
    a=[0]*N
    for j in range(10):
        
        if(t[j]=="1"):
            for k in range(N):
                
                if(int(A[k][j])==int(t[j])):
                    a[k]+=1
    T=0
    for j in range(N):
        T+=P[j][a[j]]
    MAX=max(T,MAX)

print(MAX)



