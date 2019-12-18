C=[0]*(10**5+2)
C[0]=1
C[1]=1
s=[0]*(10**5+2)
S=[0]*(10**5+2)
t=1
while(t<=(10**5)):
    t+=1
    if(C[t]==1):
        continue
    k=1
    while(True):
        k+=1
        if(t*k>(10**5)):
            break 
        C[t*k]=1

for i in range(1,(10**5),2):
    if(C[i]==0):
        if(C[(i+1)//2]==0):
            s[i]=1

for i in range(1,len(S)):
    S[i]+=s[i]+S[i-1]

N=int(input())
for i in range(N):
    l,r=map(int,input().split())
    print(S[r]-S[l-1])
