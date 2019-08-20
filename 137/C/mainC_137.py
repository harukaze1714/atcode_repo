N = int(input())

nlist=[""]*N

for i in range(N):
    t=str(input())
    t = ''.join(sorted(t))
    nlist[i] = t

cnt=1
sum=0
for i in range(N):
    cnt=1
    cnt=nlist.count(nlist[i])
    if(cnt!=1):
        sum+=cnt-1

print(int(sum/2))
