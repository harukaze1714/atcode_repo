n = int(input())
P = list(map(int, input().split()))
ans = sum(a != b for a, b in zip(P, sorted(P)))
print("YES" if ans <= 2 else "NO")


N=int(input())
A=list(map(int,input().split()))
ansa=sorted(A)
ans=0
for i in range(N-1):
  if ans==0:
    if A[i]>A[i+1]:
      ch=A[i]
      m=i
      ans=ans+1
  elif ans==1:
    if A[i]>A[i+1]:
      n=A[i+1]
      A[i+1]=ch
      A[m]=n
if A==ansa:
  print("YES")
else:
  print("NO")


N= map(int, input().split())
p = list(map(int, input().split()))
p_sort = sorted(p)
 
ans=0
for i in range(0,len(p),1):
    if(p[i]!=p_sort[i]):
        ans = ans+1
if (ans >=3):
    print("NO")
else:
    print("YES")


N = int(input())
p = list(map(int,input().split()))
c = 0
 
for i in range(N):
    if p[i] != i + 1:
        c += 1
if c <= 2:
    print('YES')
else:
    print('NO')