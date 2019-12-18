import sys
sys.setrecursionlimit(100000)

nCr = {}
def cmb(n, r):
    if n == 1: return 0
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]


N=int(input())
a=list(map(int,input().split()))

L=[0]
s=0
for i in range(N):
    s+=a[i]
    L.append(s)

L=sorted(L)

s=0
t=L[0]
c=1
for i in range(1,len(L)):
    if(t==L[i]):
        c+=1
    else:
        s+=cmb(c,2)
        t=L[i]
        c=1
else:
    s+=cmb(c,2)
print(s)
