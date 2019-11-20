N = int(input())
S = list(input())

A=[[0]*(N+1) for i in range(3)]

C=0
D=0
for i in range (1,N+1):
    if(S[i-1]=="W"):
        D+=1
    A[0][i]=D

C=0
D=0
for i in range (N-1,-1,-1):
    if(S[i]=="E"):
        C+=1
    A[1][i]=C

for i in range (N+1):
    A[2][i]=A[1][i]+A[0][i]


print(min(A[2]))