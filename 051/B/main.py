K,S=map(int,input().split())

c=0
for i in range(K+1):
    if(((i+2*K)>=S)):
        for j in range(K+1):
            if(((i+j)<=S)and((i+j+K)>=S)):
                c+=1        
print(c)
