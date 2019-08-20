N, M = map(int, input().split())

X = M-N+1
Y=N*2-1
for i in range(X,X+Y,1):
    if(i>=-1000000):
        print(i, end=" ")
