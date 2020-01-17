N=int(input())
A=list(map(int,input().split()))

c=0
for n in A:
    if(n%2==1):
        c+=1

if(c%2==0):
    print("YES")
else:
    print("NO")





