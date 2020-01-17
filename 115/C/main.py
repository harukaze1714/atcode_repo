N,K=map(int,input().split())
A=[0]*N
for i in range(N):
    A[i]=int(input())

A=sorted(A)
t=10**9
for i in range(N-K+1):
    t=min(t,abs(A[K-1+i]-A[i]))
print(t)