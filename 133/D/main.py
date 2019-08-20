N = int(input())
A = list(map(int, input().split()))

a = [0]*N

sum_a=sum(A)
a[0]=sum_a
for i in range(1,N,2):
    a[0]-=2*A[i]
print(a[0],end=" ")

for i in range(1,N):
    a[i]=2*A[i-1]-a[i-1]
    print(a[i],end=" ")
