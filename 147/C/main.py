N=int(input())
A=[0]*N
L=[[[-1]*2 for i in range (15)] for j in range (N)]
C=[1]*N
c=2**N-1
H=0
for i in range(N):
    A[i]=int(input())
    for j in range(A[i]):
        L[i][j][0],L[i][j][1]=map(int,input().split())

for i in range(c,-1,-1):
    C=list(format(i, '015b'))
    f=0
    M=C[15-N:15]
    h=0
    for e in range(N):
        h+=int(M[e])
    if(H>=h):break
    for k in range(N):
        for l in range(15):
            if(int(M[k])==0):break
            if(L[k][l][0]==-1):break
            if((int(M[L[k][l][0]-1])) != int(L[k][l][1])):
                f=1
                break
        if(f==1):
            break
    if(f==0):
        H=h

print(H)

