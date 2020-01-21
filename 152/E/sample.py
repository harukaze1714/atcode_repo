import bisect
import heapq
import random
N,M=6,13
A=[0]*N


while(True):
    for i in range(N):
        A[i]=random.randint(1,300)
    #A=[5, 6, 21, 135, 149, 164]
    A=list(sorted(A,reverse=True))

    L=[0]*N
    LIST=[]
    heapq.heapify(LIST)
    for i in range(N):
        heapq.heappush(LIST,((A[0]+A[i])*-1,i))
    s=0
    c=0
    while(M>c):
        t=heapq.heappop(LIST)
        s-=t[0]
        L[t[1]]+=1
        if(N>L[t[1]]):  
            heapq.heappush(LIST,((A[t[1]]+A[L[t[1]]])*-1,t[1]))
        c+=1
    ans1=s

    A=sorted(A)
    B=[0]*N
    B[-1]=A[-1]
    for i in range(1,N):
        B[-1-i]=B[-i]+A[-i-1]

    L=[0]*N
    Max=A[-1]*2+1
    Min=A[0]*2
    s=0

    while(s!=M):
        s=0
        l=Max
        r=Min
        C=(l+r)//2
        c=0
        for i in range(N):
            w=C-A[i]
            t=N-bisect.bisect(A,w)
            s+=t

        if(s<M):
            if(Max==C):
                break
            Max=C
        elif(s>M):
            if(Min==C):
                break
            Min=C
    #print(C,M,s)
    
    if(s-M==0):
        S=0
        for i in range(N):
            w=C-A[i]
            a=bisect.bisect(A,w)
            t=N-a
            if t>0:
                S+=t*A[i]+B[-t]
        ans2=S
    else:            
        J=0
        LISTX=[]
        cX=s-M
        C1=C
        while(cX>0):
            S=0
            for i in range(N):
                w=C-A[i]
                a=bisect.bisect(A,w)
                t=N-a
                if t>0:
                    S+=t*A[i]+B[-t]
                if(N==a):
                    a-=1
                x=A[i]+A[a]
                if x>C1 and abs(C-J)>abs(C-x):
                    J=x
            C1=J
            LISTX.append(J)
            cX-=1
        ans2=S-sum(LISTX)
    
    if ans1 != ans2:
        print(N,M)
        print(A)
        print(ans1,ans2,C)