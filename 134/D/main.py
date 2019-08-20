def make_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

N = int(input())
A = list(map(int, input().split()))
ANS = [0]*len(A)

ansList = []
for i in range(len(A),1,-1):
    if(ANS[i-1]%2!=A[i-1]):
        tList = make_divisors(i)
        #print(tList)
        for j in tList:
            ANS[j-1]+=1
        ANS[i-1]+=1
        ansList.append(i)


if(len(ansList)%2!=0):
    ANS[0]+=1
    ansList.append(1)


print(len(ansList))
for i in ansList:
    print(i, end=" ")
