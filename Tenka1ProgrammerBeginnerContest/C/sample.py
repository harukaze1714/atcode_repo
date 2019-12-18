import itertools
import random
N=1
A=[1]
while(True):
    N+=1
    u=random.randint(1,100)
    A.append(u)

    MASTER=list(itertools.permutations(A))
    s=0
    for i in range(len(MASTER)):
        t=0
        T=MASTER[i][0]
        for j in range(len(MASTER[i])):
            t+=abs(MASTER[i][j]-T)
            T=MASTER[i][j]
        if(s<t):
            B=MASTER[i]
            s=t

    print(B)
    print(s)
    #N=int(input())
    #A=[0]*N
    #for i in range(N):
    #    A[i]=int(input())

    A=sorted(A)

    mf=0
    ms=0
    sf=0
    ss=0
    d=0
    c=0
    n=0


    ml=N-1
    mr=N-1
    sl=0
    sr=1
    n=1
    while(True):
        if(n==N):break
        d+=(A[ml]-A[sl])
        ml=mr-1
        n+=1
        if(n==N):break
        d+=(A[mr]-A[sr])
        mr=ml-1
        n+=1
        if(n==N):break
        d+=(A[ml]-A[sl])
        sl=sr+1
        n+=1
        if(n==N):break
        d+=(A[mr]-A[sr])
        sr=sl+1
        n+=1

    ml=N-1
    mr=N-2
    sl=0
    sr=0
    n=1
    while(True):
        if(n==N):break
        c+=(A[ml]-A[sl])
        sl=sr+1
        n+=1
        if(n==N):break
        c+=(A[mr]-A[sr])
        sr=sl+1
        n+=1
        if(n==N):break
        c+=(A[ml]-A[sl])
        ml=mr-1
        n+=1
        if(n==N):break
        c+=(A[mr]-A[sr])
        mr=ml-1
        n+=1

    print(max(d,c))