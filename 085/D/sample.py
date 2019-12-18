N,H=map(int,input().split())
L=[[0,0,0]for i in range(N)]

for i in range(N):
    L[i][0]=i
    L[i][1],L[i][2]=map(int,input().split())
L=sorted(L,key=lambda x: (x[1],x[2]))

d=L[N-1][1]
t=N-1
k=0
for i in range(N-1,-1,-1):
    if(d!=L[i][1]):
        t=i+1
        break
L2=sorted(L,key=lambda x: (x[2],x[1]))
c=0
for i in range(N):
    if(L[t][1]<=L2[i][2]):
        break
L2=L2[i:N]
N=len(L2)

for i in range(N-1,-1,-1):
    if(L[t][1]<L2[i][2]):
        c+=1
        H-=L2[i][2]
        if(H<0):
            break
if(H>0):
    if(H%L[t][1]!=0):
        c+=1
    c+=(H//L[t][1])


print(c)
