N = int(input())
C = []
for i in range(N):
    a, b = map(int, input().split())
    C.append((a+b, a, b))

C.sort(reverse=1)

ans = 0
for i in range(N):
    _, a, b = C[i]
    if i % 2 == 0:
        ans += a
    else:
        ans -= b
print(ans)
