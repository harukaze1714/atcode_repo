import math

N= int(input())
A = list(map(int, input().split()))
 
B=[0]*N
for i in range(N):
    B[i]=A[i]-(i+1)

B=sorted(B)
cnt=B[(N//2)]

s=0
for i in range(N):
    s+=abs(B[i]-cnt)

print(s)
