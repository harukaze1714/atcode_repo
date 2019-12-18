N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

d=[0]*N
p=0
m=0
c=0
for i in range(N):
    d[i]=a[i]-b[i]
    if(d[i]>0):
        p+=d[i]
    else:
        m+=d[i]
        if(abs(d[i])%2==1):
            c+=1
m+=c

if(abs(m)>=(abs(p)*2)):
    print("Yes")
else:
    print("No")