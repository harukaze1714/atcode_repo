N = int(input())
H = list(map(int, input().split()))

for i in range(len(H)):
    H[i]=1/H[i]
sum=0
for i in range(len(H)):
    sum+=H[i]
print(1/sum)

