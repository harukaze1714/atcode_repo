N = int(input())
A=list(map(int,input().split()))
s=0
for i in range(N):
    for j in range(i+1,N):
        t=bin(A[i] ^ A[j])
        s+=int(t,0)
        s%=(10**9+7)
print(s)