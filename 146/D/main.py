N=int(input())
A=[[0,0]]*(N)
for i in range(1,N):
    A[i]=list(map(int,input().split()))
A=sorted(A)
LIST=[0]*(N+1)
for i in range(N+1):
    LIST[i]=i

MAP=[[] for i in range(N+1)]

i=1
c=0
while(N>i):
    MAP[A[i][1]].append(LIST[A[i][0]])
    MAP[A[i][0]].append(LIST[A[i][1]])    
    i+=1

LIST=[0]*(N+1)

for i in range(1,N+1):
    t=[]
    for k in range(len(MAP[i])):
        n=MAP[i]
        a=MAP[i][k]
        b=LIST[MAP[i][k]]
        t.append(LIST[MAP[i][k]])
        for j in range(len(MAP[MAP[i][k]])):
            x=MAP[MAP[i][k]]
            y=MAP[MAP[i][k]][j]
            t.append(LIST[y])
    
    j=1
    while(True):
        if t.count(j) == 0:
            LIST[i]=j
            break
        j+=1
    
print()