N=int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

total=B[A[0]-1]
for i in range(1,N):
    total+=B[A[i]-1]
    if(A[i]-1==A[i-1]):
        total+=C[A[i-1]-1]

print(total)