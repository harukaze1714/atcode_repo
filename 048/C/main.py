N,x=map(int,input().split())
A=list(map(int,input().split()))

s=0
if(A[0]>x):
    s+=A[0]-x
    A[0]=x

for i in range(N-1):
    if(A[i+1]>x):
        s+=A[i+1]-x
        A[i+1]=x
    if(A[i]+A[i+1]>x):
        t=A[i]+A[i+1]-x
        s+=t
        A[i+1]-=t

print(s)