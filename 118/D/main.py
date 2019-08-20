A = list(map(int, input().split()))
N = list(map(int, input().split()))
numList=[0,2,5,5,4,5,6,3,7,6]
dp=[[-1*(10**2),""] for i in [1] * (A[0]+11)]
    
dp[10][0]=0
for i in range(1,A[0]+1):
    tmp = [0]*10
    maxNum=-1000
    maxNums=-1000
    tmpNum=0
    for k in N:
        tmpNum=dp[10+i-numList[k]][0]+1
        if(tmpNum >= maxNum&tmpNum>=0):
            maxNum=tmpNum
            t = str(k)+str(dp[10+i-numList[k]][1])
            t = int(''.join(sorted(t, reverse=True)))
            if(t >= maxNums):
                maxNums = t
    dp[i+10][0] = maxNum
    dp[i+10][1] = maxNums
print(dp[(A[0]+10)][1])

"""
for i in range(dp[A[0]+10]):
    print("A")
"""