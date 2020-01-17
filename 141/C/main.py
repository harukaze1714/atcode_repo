N,K,Q=map(int,input().split())
L=[Q*(-1)+K]*N

for i in range(Q):
    t=int(input())
    L[t-1]+=1
t=0
for i in range(N):
    if L[i]>0:
        print("Yes")
    else:
        print("No")

