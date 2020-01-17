import sys
sys.setrecursionlimit(10**6)

N=int(input())
L=[0]*(N-1) 
MAP=[-1]*(N+1)
MAP[1]=0
for i in range(N-1):
    L[i]=list(map(int,input().split()))
    t=[L[i][1],L[i][0],L[i][2]]
    L.append(t)

L1=sorted(L,key=lambda x: (x[0],x[1]))
LIST=[[]for i in range(N+1)]

for i in range(len(L)):
    LIST[L1[i][0]].append([L1[i][1],L1[i][2]])

def calc(k):
    global MAP
    for i in range(len(LIST[k])):
        #print(LIST[k],len(LIST[k]))
        if(MAP[LIST[k][i][0]]==-1):
            MAP[LIST[k][i][0]]=(MAP[k]+LIST[k][i][1])%2
            #print(LIST[k][i][0],MAP[LIST[k][i][0]])
            calc(LIST[k][i][0])

calc(1)
for i in range(1,N+1):
    print(MAP[i])
