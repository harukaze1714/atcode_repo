import math

N = int(input())

total=0
A=[0]*N
B=[0]*N

for i in range(N):
    A[i],B[i]=map(int,input().split())

for i in range(N-1,-1,-1):
    total+=B[i]*math.ceil((A[i]+total)/B[i])-(A[i]+total)
print(total)











