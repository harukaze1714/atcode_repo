import bisect
s = input()
t = input()
lens=len(s)
lent=len(t)
d = {}
s2=s+s
lens2=len(s2)

for i in range(lens2):
    if s2[i] in d:
        d[s2[i]].append(i)
    else:
        d[s2[i]] = [i]

tmp=0
r=0
snum=0
for i in range(lent):
    if(lens<tmp):
        snum+=lens
        tmp-=lens
    if d.get(t[i],None)==None:
        print("-1")
        exit()
    else:
        lis=d[t[i]]
        r = bisect.bisect_left(lis,tmp)
        tmp=lis[r]+1
print(snum+tmp)


