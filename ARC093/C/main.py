N = int(input())
A = list(map(int, input().split()))

A.insert(0,0)
A.append(0)

B = [0]*(N+2)
C = [0]*(N+2)
total=0
last=0
simb=1

for i in range(1,N+2):
    if((A[i]-A[i-1])>0):
        C[i]=1
    elif((A[i]-A[i-1])==0):
        C[i]=C[i-1]
    else:
        C[i]=-1

for i in range(1,N+1): 
    if(C[i+1]==C[i]):
        B[i]=1
    else:
        B[i]=-1
        total+=abs(last-A[i])
        last=A[i]

total+=abs(last)

for i in range(1,N+1):
    if(B[i]==1):
        print(total)
    else:
        print(total-abs(A[i]-A[i-1])-abs(A[i+1]-A[i])+abs(A[i+1]-A[i-1]))
