N, M = map(int, input().split())
n=0
m=0
if(N!=1):
    n=2
if(M!=1):
    m=2

print(N*M-N*m-M*n+n*m)
