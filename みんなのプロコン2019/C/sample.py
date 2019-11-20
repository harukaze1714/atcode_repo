k,a,b=map(int,input().split())
ans=1
yen=0
if b<=a+2 or k<=a:
    ans+=k
else:
    n=(k-a+1)//2
    ans+=n*(b-a)+(k-2*n)
print(ans)
