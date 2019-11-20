import fractions
N, M = map(int, input().split())
X = list(map(int, input().split()))

Y=[0]*N

for i in range(N):
    Y[i]=abs(X[i]-M)

tmp=Y[0]
for i in range(N-1):
    tmp=fractions.gcd(tmp,Y[i+1])

print(tmp)
