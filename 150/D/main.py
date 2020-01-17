import fractions

N,M=map(int,input().split())
A=list(map(int,input().split()))

t=A[0]
s=1
for i in range(len(A)):
    t=fractions.gcd(t,A[i])
    s*=A[i]
s=s//t

LIST=[]

i=1
while(s*i<=M*10):
    LIST.append(s*i)
    i+=1

print()
