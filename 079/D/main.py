H,W=map(int,input().split())
A=[0]*10
dist=[10**10]*10
for i in range (10):
    A[i]=list(map(int,input().split()))

for i in range(10):
    dist[i]=A[i][1]

for k in range(10):
    for i in range(10):
        for j in range(10):
            if(dist[i]>A[i][j]+dist[j]):
                dist[i]=A[i][j]+dist[j]

s=0
for i in range (H):
    T=list(map(int,input().split()))
    for j in range(W):
        if T[j]==-1:
            continue
        else:
            s+=dist[T[j]]
print(s)

