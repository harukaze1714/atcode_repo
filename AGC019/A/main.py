A = list(map(int, input().split()))
N = int(input())

A[0]*=4
A[1]*=2
t1=10**10
for i in range(3):
   t1=min(t1,A[i])

A[0]*=2
A[1]*=2
A[2]*=2
t2=10**10
for i in range(4):
   t2=min(t2,A[i])

if(N%2==1):
    print(t2*(N//2)+t1)
else:
    print(t2*(N//2))