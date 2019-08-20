N = int(input())
H = list(map(int, input().split()))

H = sorted(H)

print(H[int(N/2)]-H[int(N/2)-1])