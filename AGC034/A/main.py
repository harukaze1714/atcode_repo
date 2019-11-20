def solve(a, b, c, d, s):
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    ss = s[a:c + 1]
    fs = s[b:d + 1]
    if '##' in ss:
        return False
    if '##' in fs:
        return False
    if c < d:
        return True
    fs2 = s[b - 1:d + 2]
    if '...' in ss and '...' in fs2:
        return True
    return False
 
 
n, a, b, c, d = list(map(int, input().split()))
s = input()
print('Yes' if solve(a, b, c, d, s) else 'No')