N, M = map(int, input().split())
numList=[[0]*2 for i in range(N)]


for i in range(N):
    A,B= map(int, input().split())
    numList[i][0]=A
    numList[i][1]=B

heap = []
ans = 0


numList =  sorted(numList, key=lambda x: (x[1]),reverse=True)
numList =  sorted(numList, key=lambda x: (x[0]))

sum=0
count=0
k=0
t=-1

for j in range(M):
    for i in range(N):
        if(numList[i][0]<=k):
            if(count<numList[i][1]):
                count=numList[i][1]
                t=i
        else:
            sum+=count
            count=0
            if(t!=-1):
                numList[t][1]=0
                t=-1
            break
    else:
        sum+=count
        count=0
        if(t!=-1):
            numList[t][1]=0
            t=-1
print(sum)