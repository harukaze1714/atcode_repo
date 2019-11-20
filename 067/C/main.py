N=int(input())

A=list(map(int,input().split()))

SUM=sum(A)
MIN=[10**10]*2
L=0
R=SUM
for i in range(N-1):
    L+=A[i]
    R-=A[i]
    if(MIN[0]>abs(L-R)):
        MIN[0]=abs(L-R)
        MIN[1]=i
print(MIN[0])