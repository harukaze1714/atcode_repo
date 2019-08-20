import math
 
N,D = map(int,input().split())
dot = [list(map(int,input().split())) for i in range(N)]
sum=0

for i in range(N):
    for j in range(i+1,N):
        tmp=0
        for k in range(D):
            tmp+=(dot[i][k]-dot[j][k])**2
        tmp=math.sqrt(tmp)
        if(float.is_integer(tmp)==True):sum+=1

print(sum)