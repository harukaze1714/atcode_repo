N = int(input())
A = []
maxNum=-1
secNum=-1
maxI=-1
for i in range(N):
    A.append(int(input()))
    if(maxNum<A[i]):
        secNum=maxNum
        maxNum=A[i]
        maxI=i
    elif(secNum<A[i]):
        secNum=A[i]

for i in range(len(A)):
    if(i!=maxI):
        print(maxNum)
    else:
        print(secNum)
