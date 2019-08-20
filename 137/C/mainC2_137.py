import math
N = int(input())

nlist=[""]*N

for i in range(N):
    t=str(input())
    t = ''.join(sorted(t))
    nlist[i] = t

sum=0
tsum=1
nlist=sorted(nlist)
tmpStr=nlist[0]
for i in range(1,N):
    if(tmpStr==nlist[i]):
        tsum+=1
    else:
        tmpStr=nlist[i]
        if(tsum!=1):
                sum+=math.factorial(tsum)/2
                tsum=1
if(tsum!=1):
        tmpStr=nlist[i]
        sum+=math.factorial(tsum)/2
        
print(int(sum))
