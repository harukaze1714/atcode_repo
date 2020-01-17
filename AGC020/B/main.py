N,M=map(int,input().split())

L = [[1,0] for i in range(N+1)]
L[1]=[1,1]

for i in range(M):
    X,Y=map(int,input().split())
    if(L[X][0]!=0):
        L[X][0]-=1
        L[Y][0]+=1
        if(L[X][1]!=0):
            L[Y][1]=1
            if(L[X][0]==0):
                 L[X][1]=0

t=0
for i in range(N+1):
    t+=L[i][1]
print(t)
