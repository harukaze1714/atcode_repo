N,T=map(int,input().split())
A=[[0,0] for i in range(N)]
for i in range(N):
    A[i][0],A[i][1]=map(int,input().split())
A=sorted(A)


def func(i,V,t):
    if(i>=N):
        return V
    if(t>=T):
        return V
    a=func(i+1,V+A[i][1],t+A[i][0])
    b=func(i+1,V,t)
    return max(a,b)
print(func(0,0,0))