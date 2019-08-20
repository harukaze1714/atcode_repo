N = int(input())
H = list(map(int, input().split()))

H.sort(reverse=True)

for i in range(len(H)):
    H[i]=H[i]/(2**(i+1))

H[len(H)-1]=H[len(H)-1]*2

print(sum(H))

