N,H=map(int,input().split())
L=[[0,0]for i in range(N)]

for i in range(N):
    L[i][0],L[i][1]=map(int,input().split())
L=sorted(L,key=lambda x: (x[0]))

d=L[N-1][0]
L2=sorted(L,key=lambda x: (x[1]))

c=0
for i in range(N-1,-1,-1):
    if(d>=L2[i][1]):
        break
    c+=1
    H-=L2[i][1]
    if(H<=0):
        break

if(H>=0):
    if(H%d!=0):
        c+=1
    c+=(H//d)


print(c)
