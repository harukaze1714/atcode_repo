import bisect

N=int(input())
A=list(map(int,input().split()))
A=sorted(A)

t=0
c=0
for i in range(N-2):
    for j in range(i+1,N-1):
        t=A[i]+A[j]
        num=bisect.bisect_left(A,t)-1
        c+=max((num-j),0)

print(c)
