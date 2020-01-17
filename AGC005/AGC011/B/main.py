N=int(input())
A=list(map(int,input().split()))

A=sorted(A)

t=A[0]
f=1
for i in range(1,N):
    if(t*2<A[i]):
        f=1
    else:
        f+=1
    t+=A[i]

print(f)
    