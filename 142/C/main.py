N=int(input())
A=list(map(int,input().split()))
L=[[0 for i in range(2)]for i in range(N)]
for i in range(N):
    L[i][0]=A[i]
    L[i][1]=i+1
L=sorted(L)

for i in range(N):
    print(L[i][1],end=" ")