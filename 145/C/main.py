N=int(input())

A=[[0,0] for i in range(N)]
B=[0]*(N*(N-1)//2)
for i in range(N):
    A[i][0],A[i][1]=map(int,input().split())
c=0
for i in range(N):
    for j in range(i+1,N):
        B[c]=((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2)**0.5
        c+=1

D=(N)*(N-1)/2

print(sum(B)*(N-1)/(D))