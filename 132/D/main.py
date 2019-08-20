import math

def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

(N, K) = input().split()
N = int(N)
K = int(K)

for i in range(1, K+1):
    if N - K + 1 < i:
        A = 0
    else:
        A = C(N - K + 1, i) * C(K - 1, i - 1) % 1000000007
    print(A)
