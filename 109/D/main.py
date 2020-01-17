H,W=map(int,input().split())
A=[0]*H
for i in range(H):
    A[i]=list(map(int,input().split()))
    for j in range(W):
        A[i][j]%=2
f=0
LIST=[]
for i in range(H):
    if(i%2==0):
        t=0
    else:
        t=W-1
    for j in range(W):
        k=abs(j-t)
        if(A[i][k]==1):
            if(f==1):
                q=i
                w=k
                while(True):
                    T=[]
                    T.append(a+1)
                    T.append(b+1)
                    if((b==0 and a%2==1) or (b==(W-1) and a%2==0)):
                        a+=1
                    elif(a%2==0):
                        b+=1
                    else:
                        b-=1
                    T.append(a+1)
                    T.append(b+1)
                    LIST.append(T)                        
                    if(q==a and w==b):
                        f=0
                        A[a][b]=0
                        break
                    
            else:
                a=i
                b=k
                A[a][b]=0
                f=1
        
print(len(LIST))
for i in range(len(LIST)):
    T=""
    for j in range(len(LIST[i])):
        T=T+str(LIST[i][j])+" "
    print(T[0:-1])
