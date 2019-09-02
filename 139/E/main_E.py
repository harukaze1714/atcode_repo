N = int(input())
H = [0]*N
A = [0]*N
A2 = [0]*N
flag=0
flag2=0
for i in range(N):
    H[i] = list(map(int, input().split()))

k=0
while(True):
    k+=1
    for i in range(N):
        if(A[i]==0):
            if(A[H[i][0]-1]==0):
                if(H[H[i][0]-1][0]==i+1):
                    A[i]=1
                    A[H[i][0]-1]=1
                    if(len(H[H[i][0]-1])==1):
                        A2[H[i][0]-1]=1
                    if(len(H[i])==1):
                        A2[i]=1

                    H[H[i][0]-1].pop(0)
                    H[i].pop(0)
                    
                    flag2=0

    for j in range(N):
        A[j] = A2[j]
        if(A2[j]==0):
            flag=0
    
    if(flag==1):
        break
    if(flag2==1):
        break
    
    flag=1
    flag2=1

if(flag2==1):
    print("-1")
    exit()

print(k)
