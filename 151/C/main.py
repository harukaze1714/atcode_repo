N,M=map(int,input().split())
LIST=[0]*(10**5+1)
PLIST=[0]*(10**5+1)

C=0
P=0
for i in range(M):
    A=list(map(str,input().split()))
    if(A[1]=="WA"):
        if(LIST[int(A[0])]==0):
            PLIST[int(A[0])]+=1
    else:
        if(LIST[int(A[0])]==0):
            C+=1
            LIST[int(A[0])]=1

for i in range(len(LIST)):
    P+=LIST[i]*PLIST[i]

print(C,P)
