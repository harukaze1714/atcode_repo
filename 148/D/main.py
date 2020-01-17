N=int(input())
A=list(map(int,input().split()))

t=1
for i in range(len(A)):
    if(A[i]==t):
        t+=1
if(t==1):
    print(-1)
else:   
    print(N+1-t)