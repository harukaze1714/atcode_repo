r,g,b,n=map(int,input().split())

rr=n//r
tmp=0
for i in range(rr+1):
    gg=(n-i*r)//b
    for j in range(gg+1):
        if((n-r*i+g*j)%b==0):
            tmp+=1
print(tmp)
