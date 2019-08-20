def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    divisors.reverse()
    return divisors

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0]
"""
for para in A:
    print(para)

for num,para in enumerate(B):
    print(C)
"""

#print(max(B))
maxB = max(B)
sumNum = 9999999999
tSumNum = 0
ansNum = 0

for i in range(maxB,0,-1):
    tsum=0
    for j,bNum in enumerate(B):
        for k in range(0,9999999):
            if(bNum<i*k):break
            tnum=abs(bNum-i*k)
            #print(i,bNum,k,abs(bNum-i*k))
        tsum+=tnum
        #print(tsum)
    print(i,tsum)
        