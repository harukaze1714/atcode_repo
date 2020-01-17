N=int(input())
A=list(map(int,input().split()))
LIST=[0]*N
B=[0]*N
i=0
c=0
while(i<3**N):
    LIST[0]=i
    for j in range(N):
        if j!=N-1:
            LIST[j+1]=LIST[j]//3
        LIST[j]=LIST[j]%3
    z=0
    o=0
    t=0
    f=0
    for j in range(N):
        if(LIST[j]==0):
            if(A[j]==z):
                z+=1
            else:
                f=1
                break
        if(LIST[j]==1):
            if(A[j]==o):
                o+=1
            else:
                f=1
                break
        if(LIST[j]==2):
            if(A[j]==t):
                t+=1
            else:
                f=1
                break


    if(f==0):
        c+=1
        c%=1000000007
        #print(LIST)
    i+=1
print(c)



