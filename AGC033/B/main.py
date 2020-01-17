s = input().replace('BC', 'D')
 
acc = 0
ans = 0
for c in s:
    if c == 'B' or c == 'C':
        acc = 0
        continue
    elif c == 'A':
        acc += 1
    else:
        ans += acc
print(ans)