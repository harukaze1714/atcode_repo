N=list(input())

l=0
r=len(N)-1

c=0
while(True):
    if(r<=l):
        print(c)
        exit()
    
    if(N[l]==N[r]):
        l+=1
        r-=1
    elif(N[l]=="x" and N[r]!="x"):
        l+=1
        c+=1
    elif(N[l]!="x" and N[r]=="x"):
        r-=1
        c+=1
    else:
        print(-1)
        exit()