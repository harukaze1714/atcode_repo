N,K=map(int,input().split())
S=input()

#K=1
#S="01100"
#N=len(S)

LIST=[[[0] for j in range (2)]for i in range(N)]

t=S[0]
c=0
k=0
for i in range(N):
    if(t!=S[i]):
        LIST[k][0]=c
        LIST[k][1]=t
        t=S[i]
        k+=1
        c=0
    c+=1

LIST[k][0]=c
LIST[k][1]=t
LIST=LIST[0:k+1]
MAX=0

s=0
l=0
r=0

if(LIST[r][1]=="1"):
    s+=LIST[r][0]
    r+=1
x=0
while(K>0 and len(LIST)>r):
    s+=LIST[r][0]
    K-=1
    if(len(LIST)-1==r):
        x=1
        break
    r+=1
    s+=LIST[r][0]
    if(len(LIST)-1==r):
        x=1
        break
    r+=1

MAX=max(s,MAX)

f=0
if(x==0):
    while(r<len(LIST)):
        if(l< len(LIST)-1):
            s-=LIST[l][0]
            l+=1
            f=1
        if(l<len(LIST)-1 and LIST[l][1]=="0"):
            s-=LIST[l][0]
            l+=1

        if(f==0):
            break
        

        s+=LIST[r][0]
        MAX=max(s,MAX)
        r+=1
        if(len(LIST)==r):
            break
        
        s+=LIST[r][0]
        MAX=max(s,MAX)
        r+=1
        if(len(LIST)==r):
            break

print(MAX)
