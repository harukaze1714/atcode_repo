n,m=map(int,input().split())
s=[list(map(int,input().split()))for i in range(m)]
for i in range(m):
    del s[i][0]
p=list(map(int, input().split()))
q=[0]*11


ans=0
while(True):
    for i in range(n):
        if(q[i]==2):
            q[i+1]+=1
            q[i]=0
    if(q[n]==1):
        break
    
    flag=1
    for i in range(m):
        tmp=0
        for j in s[i]:
            tmp+=q[j-1]
        if(tmp%2!=p[i]):
            flag=0
            break
    if(flag==1):
        ans+=1
    q[0]+=1

print(ans)

