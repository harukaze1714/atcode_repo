N, K = map(int, input().split())
A = list(map(int, input().split()))
 
 
import math
 
 
ans = math.ceil((N-K) / (K - 1)) + 1
print(ans)
 
"""
#print(A)
#print(A.index(min(A)))
m=min(A)
a=A.index(m)

i=a
tmp=0
while(i<N):
    while(A[i]==m):
        if(i>=N):
            break
        i+=1
    if(i>=N):
        break
    #for k in range(K-1):
        #A[i+k]=m
    tmp+=1
    i+=K-1

tmp+=math.ceil(a/(K-1))

print(tmp)


ml=[i for i, v in enumerate(A) if v == min(A)]
#print(minlist)
tmp=0

tmp+=math.ceil(ml[0]/(K-1))
for i in range(len(ml)-2):
    tmp+=math.ceil((ml[i+1]-ml[i]-1)/(K-1))
tmp+=math.ceil((N-ml[len(ml)-1]-1)/(K-1))
print(tmp)
"""