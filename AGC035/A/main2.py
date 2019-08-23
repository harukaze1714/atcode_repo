N = int(input())
L = list(map(int, input().split()))

total=L[0]
for i in range(1,N):
    total^=L[i]

if(total==0):
    print("Yes")
else:
    print("No")