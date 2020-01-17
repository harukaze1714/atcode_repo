from queue import Queue
NUM=9*(10**10)
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
MAP=[[NUM]*N for i in range(N)]
F=0
q = Queue()

for i in range(N-1):
    MAP[A[i][0]][A[i][1]]=A[i][2]
    MAP[A[i][1]][A[i][0]]=A[i][2]
F=0
for z in Z:
    q = Queue()
    if(MAP[z[0]][K]==NUM):
        for i in range(N):
            if(MAP[z[0]][i]!=NUM):
                q.put((MAP[z[0]][i],i))
    while not q.empty():
        T=q.get()
        if(MAP[T[1]][K]!=NUM):
            c=T[0]+MAP[T[1]][K]
            if MAP[z[0]][K] > c:
                MAP[z[0]][K]=c
                break
        for i in range(N):
            if(MAP[T[1]][i]!=NUM):
                q.put((T[0]+MAP[T[1]][i],i))
    
    q = Queue()
    if(MAP[z[1]][K]==NUM):
        for i in range(N):
            if(MAP[z[1]][i]!=NUM):
                q.put((MAP[z[1]][i],i))
    while not q.empty():
        T=q.get()
        if(MAP[T[1]][K]!=NUM):
            c=T[0]+MAP[T[1]][K]
            if MAP[z[1]][K] > c:
                MAP[z[1]][K]=c
                break
        for i in range(N):
            if(MAP[T[1]][i]!=NUM):
                q.put((T[0]+MAP[T[1]][i],i))

for z in Z:
    print(MAP[z[0]][K]+MAP[z[1]][K])



