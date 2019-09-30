N = int(input())
P = list(map(int, input().split()))
L = [0]*N


for i in range(N):
    L[N-(P[i])]=i

total = 0
for i in range(N):
    for j in range(i+1,N):
        flag=0
        #print(i+1,j+1)
        for k in range(N):
            if((L[k]>=i)&(L[k]<=j)):
                flag+=1
            if(flag==2):
                total+=(N-k)
                break
print(total)
        


    

