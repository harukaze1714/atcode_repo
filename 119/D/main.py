N = list(map(int, input().split()))
#A = [[0] * (N[0]+N[1]+N[2])]*2
A = [[10**11+1] * 4 for i in range((N[0]+N[1]+N[2]))]
#print(A)
for i in range(N[0]):
    A[i][0]=int(input())
    A[i][1]=0

for i in range(N[0],N[0]+N[1]):
    A[i][0]=int(input())
    A[i][1]=1

r=0
for i in range(N[0]+N[1],N[0]+N[1]+N[2]):
    A[i][0]=int(input())
    A[i][1]=2
    A[i][2]=r
    r+=1

A=sorted(A)
#print(A)

L0=10**11+1
R0=10**11+1

L1=10**11+1
R1=10**11+1

j=0

for i in range(N[0]+N[1]+N[2]):
    k=i
    R0=10**11+1
    R1=10**11+1
    if(A[i][1]==0):L0=A[i][0]
    if(A[i][1]==1):L1=A[i][0]
    if(A[i][1]==2):
        for j in range(k,N[0]+N[1]+N[2]):
            if(A[j][1]==0):
                R0=A[j][0]
            if(A[j][1]==1):
                R1=A[j][0]
            if((R0!=(10**11+1))&(R1!=(10**11+1))):break
        LA01=abs(L0-A[i][0])
        RA01=abs(R0-A[i][0])
        LA11=abs(L1-A[i][0])
        RA11=abs(R1-A[i][0])
        LA02=LA01*2
        RA02=RA01*2
        LA12=LA11*2
        RA12=RA11*2

        #print(min(max(LA01,LA11),LA01+RA12,RA01+LA12,max(RA01,RA11),max(LA01,LA11),LA02+RA11,RA02+LA11,max(RA01,RA11)))
        A[i][3]=min(max(LA01,LA11),LA01+RA12,RA01+LA12,max(RA01,RA11),LA02+RA11,RA02+LA11)

A=sorted(A, key=lambda x: x[2])

for i in range(N[2]):
    print(A[i][3])

