N = int(input())
A = list(map(int, input().split()))

A=sorted(A)
maxA=max(A)
limit=maxA/2
tmp=10**9
for i in range(N):
    if(abs(limit-A[i])<tmp):
        tmp=abs(limit-A[i])
        comb=A[i]
    else:
        break

print(maxA,comb)