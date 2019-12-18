N,M=map(int,input().split())
A=[0]*N
B=[0]*M
C=[[0]*N for i in range(N)]
D=[[0]*N for i in range(N)]

for i in range(N):
    A[i]=list(input())
for i in range(M):
    B[i]=list(input())

SUM=0
for i in range(M):
    for j in range(M):
        if(B[i][j]=="#"):
            SUM+=1

for k in range(N):
    t=0
    for i in range(M):
        if(A[k][i]=="#"):
            t+=1
    C[k][i-M+1]=t
    for i in range(M,N):
        if(A[k][i]=="#"):
            t+=1
        if(A[k][i-M]=="#"):
            t-=1
        C[k][i-M+1]=t
for i in range(N):
    for j in range(N-M+1):
        for k in range(M):
            D[j][i]+=C[j+k][i]

for i in range(N-M+1):
    for j in range(N-M+1):
        if(D[i][j]==SUM):
            e=1
            for k in range(M):
                for l in range(M):
                    if(A[i+l][j+k]!=B[k][l]):
                        e=0  
            if(e==1):
                print("Yes")
                exit()
print("No")
