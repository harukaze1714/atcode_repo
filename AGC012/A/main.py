N = int(input())
A = list(map(int, input().split()))

A=sorted(A)

t=0
for i in range(N):
    a=A[3*N-i*2-2]
    t+=a
print(t)