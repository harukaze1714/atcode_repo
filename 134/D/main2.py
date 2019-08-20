import math as math

N = int(input())
A = list(map(int, input().split()))
ANS = [0]*len(A)
for i in range(math.floor(N/2)+1,N):
    ANS[i] = A[i]

fnum=math.floor(N/2)
for i in range(fnum,-1,-1):
    j = i + 1
    tsum=A[i]
    for k in range(j,N+1,j):
        tsum+=ANS[k-1]
    ANS[i]=tsum%2

#print(ANS)
anslist=[]
for i in range(N):
    if ANS[i]==1:
        anslist.append(i+1)
 
print(len(anslist))
for s in anslist:
    print(s, end =" ")

