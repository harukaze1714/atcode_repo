N=int(input())
C=[0]*N
S=[0]*N
F=[0]*N

for i in range(N-1):
    C[i],S[i],F[i]=map(int,input().split())

def calc(n):
    t=0
    for i in range(n,N-1):
        if(t<S[i]):
            t=S[i]
        if(t%F[i]!=0):
            t+=(F[i]-t%F[i])
        t+=C[i]
    print(t)


for i in range(N):
    calc(i)