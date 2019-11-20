import math

n,m=map(int,input().split())

if(abs(n-m)>1):
    print(0)
    exit()

N=math.factorial(n)
M=math.factorial(m)
if(abs(n-m)==1):
    print((N*M)%(10**9+7))
else:
    print((N*M*2)%(10**9+7))
