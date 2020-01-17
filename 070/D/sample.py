N=int(input())
A=[0]*(N-1)
for i in range(N-1):
    A[i]=list(map(int,input().split()))
    A[i][0]-=1
    A[i][1]-=1
Q,K=map(int,input().split())
K-=1
Z=[0]*(Q)
for i in range(Q):
    Z[i]=list(map(int,input().split()))
    Z[i][0]-=1
    Z[i][1]-=1
MAP=[[10**5]*N for i in range(N)]
MAP2=[[10**5]*N for i in range(N)]

for i in range(N-1):
    MAP[A[i][0]][A[i][1]]=A[i][2]
    MAP[A[i][1]][A[i][0]]=A[i][2]

def cal(x1,x2,c,o,f,T):
    M=MAP
    M2=MAP2
    global K
    if(f==0):
        if(x1==x2 and MAP2[o][x2]>c):
            MAP2[o][x2]=c
            return 0
        if(MAP2[o][x2]<c):
            return 0
    if(f==1):
        if(x1==K):
            f=0
            T=[0,1,2,3,4]
        if(MAP2[o][x2]<c):
            return 0

    for i in T:
        if MAP[x1][i] != 10**5:
            if MAP[x1][i] == 10**5:
                k=0
            else:
                k=MAP[x1][i]
            T1=T[:]
            T1.remove(i)
            cal(i,x2,c+k,o,f,T1)

    return 0

T=[i for i in range(N)]
for i in Z:
    T1=T[:]
    T1.remove(i[0])
    cal(i[0],i[1],0,i[0],1,T1)

for i in Z:
    print(MAP2[i[0]][i[1]])
#print()

