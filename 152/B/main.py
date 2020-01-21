N,M,K=map(int,input().split())
A=list(map(int,input().split()))

ALL=N*K
S=sum(A)
S=ALL-S

if(M>=S):
    print(max(0,S))
else:
    print("-1")