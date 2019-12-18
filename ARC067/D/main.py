N,A,B=map(int,input().split())
X=list(map(int,input().split()))

L=[0]*(N-1)
s=0
for i in range(N-1):
    L[i]=X[i+1]-X[i]
    if(A*L[i]>=B):
        s+=B
    else:
        s+=A*L[i]
print(s)