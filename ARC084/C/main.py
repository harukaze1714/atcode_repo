N=6
#A=[3,14,159,2,6,53]
#B=[58,9,79,323,84,6]
#C=[2643,383,2,79,50,288]
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

D=[0]*N
E=[0]*N

A=list(sorted(A,reverse=True))
B=list(sorted(B,reverse=True))
C=list(sorted(C,reverse=True))

u=N-1
d=N-1
c=0
while(True):
    if A[u] < B[d]:
        c+=1
        u-=1
    else:
        D[d]=c
        d-=1
    if(-1==u or -1==d):
        for i in range(d,-1,-1):
            D[i]=c
        break
u=0
d=0
c=0
while(True):
    if B[u] < C[d]:
        c+=1
        d+=1
    else:
        E[u]=c
        u+=1
    if(N==u or N==d):
        for i in range(u,N):
            E[i]=c
        break

s=0
for i in range(N):
    s+=D[i]*E[i]


print(s)