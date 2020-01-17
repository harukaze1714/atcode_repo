import collections
N, P = map(int, input().split())

i=2
a=[]
ans=1
while(True):
    if(P%i==0):
        P=P//i
        a.append(i)
    else:
        break

i=3 
while(True):
    if(P%i==0):
        P=P//i
        a.append(i)
        c=1
    else:
        i+=2
        c=0

    if((P<i**N)&(c==0)):
        break

dct=collections.Counter(a)

li=dct.items()

for tt in li:
    if tt[1]>=N:
        ans*=tt[0]**(tt[1]//N)

print(ans)    