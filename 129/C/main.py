N,K = map(int,input().split())
NUM=[0]*N
bunsu=[0]*N

for i in range(N):
    for j in range(0,2**10):
        total=(i+1)*(2**j)
        if(total>=K):
            break

    bunsu[i]=1/(N*(2**j))

print(sum(bunsu))
