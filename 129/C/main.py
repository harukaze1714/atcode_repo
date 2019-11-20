MOD=10**9+7
N,M=map(int,input().split())
A=[True]*(N+2)

for i in range(M):
    a=(int(input())+1)
    A[a]=False

S=[0]*(N+2)
S[1]=1
for i in range(2,N+2):
    if(A[i]):
        S[i]=(S[i-1]+S[i-2])%MOD
    else:
        S[i]=0
print(S[N+1])