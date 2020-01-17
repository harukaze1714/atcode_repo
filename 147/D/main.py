N = int(input())
A=list(map(int,input().split()))
L=[0]*65
MOD=(10**9+7)
for i in range(N):
    t=str(format(A[i],"b"))
    for j in range(len(t)):
        L[j]+=int(t[-j-1])

for i in range(len(L)):
    L[i]=L[i]*(N-L[i])
    L[i]*=2**i
    L[i]%=MOD
print(sum(L)%MOD)


