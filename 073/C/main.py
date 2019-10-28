import collections

N = int(input())

List = {}
for i in range(N):
    A = int(input())
    if List.get(A,None)==None:
        List[A]=1
    else:
        del List[A]

c = collections.Counter(List)

print(len(c))
