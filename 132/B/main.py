N = int(input())
H = list(map(int, input().split()))

sum=0
for i in range(1,N-1):
    if(min(H[i-1],H[i],H[i+1])!=H[i]):
        if(max(H[i-1],H[i],H[i+1])!=H[i]):
            sum+=1
print(sum)