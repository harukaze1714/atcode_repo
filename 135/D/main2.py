import numpy as np

A = list(input())
NUM=13

DP = np.zeros((len(A),NUM), dtype=np.int64)
ANS = np.zeros(NUM, dtype=np.int64)

for i in range(len(A)):
        if(A[i]=="?"):
                for j in range(10):
                        DP[i][(j*(10**(len(A)-i-1)))%NUM]+=1
        else:
                DP[i][(int(A[i])*(10**(len(A)-i-1)))%NUM]+=1

for i in range(len(A)-1,0,-1):    
        for j in range(NUM):
                for k in range(NUM):
                        ANS[j] += DP[i][(k)%NUM]*DP[i-1][(NUM-k+j)%NUM]
                ANS[j]=ANS[j]%(10**9+7)
        DP[i-1] = ANS[:]
        ANS = [0]*NUM

ANS = DP[0][:]
print(ANS[5])


