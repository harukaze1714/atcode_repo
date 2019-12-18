import math
 
N,M=map(int,input().split())

for i in range(M//N +1,0,-1):
    if(M%i==0):
        if((M//i)>=N):
            print(i)
            exit()
