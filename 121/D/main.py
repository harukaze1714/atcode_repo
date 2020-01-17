import math
l,r=map(int,input().split())

t=r
c=0
while(t!=0):
    c+=1
    t//=2
LIST=[0]*c

if(c==0):
    print(0)
    exit()

l=l-1

t1=math.ceil(l/2)
t2=math.ceil(r/2)
LIST[-1]=((t2-t1)%2)*(2**(0))

for i in range(2,c+1):
    k=(l-(l//2**i)*(2**i))+1
    t1=max(k-((2**i)//2),0)

    k=(r-(r//2**i)*(2**i))+1
    t2=max(k-((2**i)//2),0)
 
    LIST[-i]=((t2-t1)%2)*(2**(i-1))

print(sum(LIST))