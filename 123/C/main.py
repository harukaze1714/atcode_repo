import math

N = int(input())
M=10**20
for i in range(5):
    M=min(M,int(input()))

if(M>=N):
    print(5)
else:
    print(math.ceil(N/M)+4)

