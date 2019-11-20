N = int(input())
A = list(map(int, input().split()))

B=[]

if(N%2==0):
    for i in range(N-1,-1,-2):
        print(A[i],end=" ")
    for i in range(0,N,2):
        print(A[i],end=" ")
        
else:
    for i in range(N-1,-1,-2):
        print(A[i],end=" ")
    for i in range(1,N,2):
        print(A[i],end=" ")
