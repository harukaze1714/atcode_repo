N=int(input())
L=list(map(int,input().split()))
c=0
s=0
mi=10**10
for i in range(N):
    if(L[i]<0):
        c+=1
    s+=abs(L[i])
    if(abs(L[i])<mi):
        mi=abs(L[i])
if(c%2==0):
    print(s)
    exit()
print(s-(2*mi))