import fractions
import bisect

N,M = map(int,input().split())
S=input()
T=input()

A=(N//fractions.gcd(N,M))*M

NL=[0]*N
ML=[0]*M

for i in range(N):
    NL[i]=i*(A//N)


for i in range(M):
    ML[i]=i*(A//M)


ANDL = sorted(list(set(NL) & set(ML)))

for i in ANDL:
    St=bisect.bisect_left(NL,i)
    Tt=bisect.bisect_left(ML,i)
    if(S[St]!=T[Tt]):
        print("-1")
        exit()
print(A)
