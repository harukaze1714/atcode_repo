N,Q = map(int, input().split())

A=[[0]*2 for i in range(N)]
Ans=[0]*(N+1)
P=[[0]*2 for i in range(Q)]

for i in range(N-1):
    A[i][0],A[i][1] = map(int, input().split())
for i in range(Q):
    P[i][0],P[i][1] = map(int, input().split())
    Ans[P[i][0]]+=P[i][1]

A.sort()

for i in range(N):
    Ans[A[i][1]]+=Ans[A[i][0]]

for i in range(1,N+1):
    print(Ans[i],end=" ")
