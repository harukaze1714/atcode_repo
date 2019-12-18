N,M=map(int,input().split())
L=[[0 for i in range(4)]for i in range(M)]
for i in range(M):
    a,b=map(int,input().split())
    L[i][0]=i
    L[i][1]=a
    L[i][2]=b
L2=sorted(L,key= lambda x: (x[1],x[2]))

c=0
t=0
for i in range(M):
    if(L2[i][1]!=c):
        c=L2[i][1]
        t=1
    L2[i][3]=t
    t+=1

L3=sorted(L2,key= lambda x: (x[0]))

for i in range(M):
    print('{0:06d}'.format(L3[i][1]),'{0:06d}'.format(L3[i][3]),sep="")