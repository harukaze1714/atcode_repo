N, M = map(int, input().split())
A = list(map(int, input().split()))

A=sorted(A)
B=[0]*(M-1)

for i in range(len(A)-1):
    B[i]=A[i+1]-A[i]

B=sorted(B)
if(N>=M):
    print("0")
    exit()
else:
    print(sum(B[0:M-N]))