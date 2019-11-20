MOD=10**9+7

N , K = map(int,input().split())
A = list(map(int,input().split()))

B=A+A
C=[0]*N
D=[0]*N

for i in range(N):
    for j in range(i,2*N):
        if(B[i]>B[j]):
            C[i]+=1
for i in range(N):
    for j in range(i,N):
        if(B[i]>B[j]):
            D[i]+=1

c=sum(C)%MOD
d=sum(D)%MOD
c=(c-d)%MOD
t=((K*(2*d+((K-1)*c)))//2)%MOD

print(t)