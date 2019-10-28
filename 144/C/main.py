import math
N = int(input())
N2 =  int(math.sqrt(N))

for i in range(N2,0,-1):
    if(N%i==0):
        print(N//i+i-2)
        exit()

print(N-1)