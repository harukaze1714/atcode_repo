import math
L, R = map(int, input().split())
R=min(R,L+2019)
m=2018
for i in range(L,R+1):
  for j in range(i,R+1):
    if i==j:
      continue
    if (i*j)%2019<m:
      m=(i*j)%2019
print(m)