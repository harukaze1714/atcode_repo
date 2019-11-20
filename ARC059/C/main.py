N=int(input())
A=list(map(int,input().split()))

ave=round((sum(A)/N))

t=0
for a in A:
    t+=(a-ave)**2
print(t)