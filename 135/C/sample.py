N = int(input())
B = list(map(int,input().split()))
C = list(map(int,input().split()))

tmp=0
cnt=0
for i in range(N):
    tmp = B[i]-C[i]
    if(tmp>0):
        cnt+=C[i]
        B[i]-=C[i]
        C[i]=0
    else:
        cnt+=B[i]
        C[i]-=B[i]
        B[i]=0

    tmp = B[i+1]-C[i]
    if(tmp>0):
        cnt+=C[i]
        B[i+1]-=C[i]
        C[i]=0
        
    else:
        cnt+=B[i+1]
        C[i]-=B[i+1]
        B[i+1]=0

print(cnt)
        
