import math
N = int(input())

nlist=[""]*N
d={}
for i in range(N):
    t=str(input())
    t=''.join(sorted(t))
    if d.get(t,None)==None:
        d[t]=1
    else:
        d[t]+=1 
ans=0

#print(d.keys(),d.values())
for i in d.values():
    ans += i*(i-1)/2
print(int(ans))
