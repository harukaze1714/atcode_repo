#N,K=map(int,input().split())
#S=input()
import random
e=0
S=["0","1","0","1"]

while(True):
    e+=1
    K=max(1,e//3)
    S.append(str(random.randint(0,1)))
    N=len(S)

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
    f=0
    if(LIST[0][1]=="1"):
        s+=LIST[0][0]
        l=0
        r=1
        f=1
    MAX=0

    while(K>0):
        s+=LIST[r][0]
        K-=1
        if(len(LIST)-1==r):
            break
        r+=1
        s+=LIST[r][0]
        if(len(LIST)-1==r):
            break
        r+=1

    if f==1:
        while(r<N):
            s-=LIST[l][0]
            l+=1
            s-=LIST[l][0]
            l+=1

            s+=LIST[r][0]
            MAX=max(s,MAX)
            if(len(LIST)-1==r):
                break
            r+=1
            s+=LIST[r][0]
            MAX=max(s,MAX)
            if(len(LIST)-1==r):
                break
            r+=1
    else:
        s-=LIST[l][0]
        l+=1

        s+=LIST[r][0]
        MAX=max(s,MAX)
        if(len(LIST)-1==r):
            print(MAX)
            continue
        r+=1
        s+=LIST[r][0]
        MAX=max(s,MAX)
        if(len(LIST)-1==r):
            print(MAX)
            continue
        r+=1
        while(r<N):
            s-=LIST[l][0]
            l+=1
            s-=LIST[l][0]
            l+=1

            s+=LIST[r][0]
            MAX=max(s,MAX)
            if(len(LIST)-1==r):
                break
            r+=1
            s+=LIST[r][0]
            MAX=max(s,MAX)
            if(len(LIST)-1==r):
                break
            r+=1

    print(MAX)
