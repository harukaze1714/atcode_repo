N=int(input())
A=list(map(int,input().split()))
D={}

s=0
for i in range(N):
    if D.get(A[i],None)==None:
        D[A[i]]=1
    else:
        D[A[i]]+=1
        s+=1

if s%2==1:
    print(N-s-1)
else:
    print(N-s)