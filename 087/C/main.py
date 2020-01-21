N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
LA=[0]*N
LB=[0]*N
LA[0]=A[0]
LB[-1]=B[-1]

for i in range(N-1):
    LA[i+1]=LA[i]+A[i+1]
    LB[-i-2]=LB[-i-1]+B[-i-2]
c=0
for i in range(N):
    c=max(c,LA[i]+LB[i])
print(c)