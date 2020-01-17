N=int(input())
A=[0]*N
for i in range(N):
    A[i]=int(input())
f=0
for i in range(N):
    if A[i]%2==1:
        f=1

if(f==0):
    print("second")
else:
    print("first")
