import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v, p = [int(item) for item in input().split()]
a = [int(item) for item in input().split()]
a.sort()
cumsum = [0] * (n+1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + a[i]

hand = n - v 
ok = [0] * (n - p)
for i in range(n - p):
    total = cumsum[n-p+1] - cumsum[i+1] - a[i] * (n - p - i)
    maxval = a[n-p] - a[i]
    turn = max((total + hand - 1) // hand, maxval)
    if m >= turn:
        ok[i] = 1
ans = sum(ok) + p
print(ans)
