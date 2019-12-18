N=int(input())
X=[0]*N
Y=[0]*N
LIST=[[0,0] for i in range(N*N)]
for i in range(N):
    X[i],Y[i]=map(int,input().split())

for i in range(N):
    for j in range(N):
        if(i==j):continue
        LIST[i*N+j][0]=X[i]-X[j]
        LIST[i*N+j][1]=Y[i]-Y[j]

LIST=sorted(LIST,key=lambda x: (x[0],x[1]))

t=[0,0]
m=0
c=0
for i in range(len(LIST)):
    if(LIST[i]==[0,0]):continue
    elif(LIST[i]!=t):
        c=1
        t=LIST[i]
    else:c+=1
    m=max(c,m)

print(N-m)