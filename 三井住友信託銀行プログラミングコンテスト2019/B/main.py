import math

N = int(input())
D={}
T=list(map(int,input().split()))
if(T[0]!=0):
        print("0")
        exit()

for i in range(N):
    if D.get(T[i],None)==None:
        D[T[i]]=1
    else:
        D[T[i]]+=1

Max=max(D)
Min=min(D)
Len=len(D)
Item=sorted((D.items()))
if(Item[0][1]!=1):
        print("0")
        exit()
for i in range(Len):
    if(Item[i][0]!=i):
        print("0")
        exit()
ans=1
for i in range(1,Len):
    ans = (ans * (Item[i-1][1]**Item[i][1])) % 998244353
    
print(ans)