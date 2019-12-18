n = int(input())
s = input()
ans = 0
for a in range(10):
  for b in range(10):
    for c in range(10):
      a, b, c = str(a), str(b), str(c)
      a_find = s.find(a)
      if a_find == -1:
        continue
      b_find = s.find(b, a_find + 1)
      if b_find == -1:
        continue
      c_find = s.find(c, b_find + 1)
      if c_find == -1:
        continue
      ans += 1
print(ans)