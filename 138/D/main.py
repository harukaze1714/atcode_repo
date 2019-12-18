import sys

N,Q = [int(i) for i in sys.stdin.readline().split()]
#D=[10**10]*N
#D[0]=0
A=[[10**10]*3 for i in range(N-1)]
A[0][2]=0
Ans=[0]*N
P=[[0]*2 for i in range(Q)]

for i in range(N-1):
    A[i][0],A[i][1] = [int(i) for i in sys.stdin.readline().split()]
    if(A[i][0]==1):
        A[i][2]=1
    else:
        if(A[i][0]<(10**10)):
            A[i][2]=A[A[i][0]-1][2]+1
while(A>(10**10)):
    for i in range(N-2,-1,-1):
        if(A[i][2]>(10**10)):
            A[i][2]=A[A[i][0]-1][2]+1


for i in range(Q):
    P[i][0],P[i][1] = [int(i) for i in sys.stdin.readline().split()]
    Ans[P[i][0]-1]+=P[i][1]
A=sorted(A,key=lambda x: x[2])

for i in range (N-1):
    Ans[A[i][1]-1]+=Ans[A[i][0]-1]
print(*Ans)
