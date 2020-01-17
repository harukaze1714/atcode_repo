import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)
B=[0]*N
B[-1]=A[-1]
for i in range(1,N):
    B[-1-i]=B[-i]+A[-i-1]

L=[0]*N
Max=A[-1]*2+1
Min=A[0]*2
s=0
f=0
if(N==1):
    print(A[0]*2)
    exit()

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
            f=1
            break
        Max=C
    elif(s>M):
        if(Min==C):
            break
        Min=C
#print(C,M,s)
ans=0
S=0
if(s-M==0):
        S=0
        for i in range(N):
            w=C-A[i]
            a=bisect.bisect(A,w)
            t=N-a
            if t>0:
                S+=t*A[i]+B[-t]
        ans=S
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
    ans=S-sum(LISTX)

print(ans)