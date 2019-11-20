n = int(input())
s = input()
l = {}
for c in s:
    if c in l:
        l[c] += 1
    else:
        l[c] = 1
ans = 1
for i in l.values():
    ans *= i+1
print((ans-1)%(10**9+7))