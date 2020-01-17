import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

A = list(range(1, N + 1))
for i, x in enumerate(itertools.permutations(A)):
    if list(x) == P:
        pn = i
    if list(x) == Q:
        qn = i
print(abs(pn - qn))
