import collections

n,p=map(int,input().split())

a=[]
while p % 2 == 0:
  p //= 2
  a.append(2)
f = 3

while f * f <= p:
  if p % f == 0:
    a.append(f)
    p //= f
  else:
    f += 2
if p != 1:
  a.append(p)

dct=collections.Counter(a)

ans=1

li=dct.items()

for tt in li:
  if tt[1]//n>=1:
    ans*=tt[0]**(tt[1]//n)
print(ans)
