def calc(N):
    L=[]
    for i in range(1,int(N**0.5) + 1):
        if(N%i==0):
            L.append(i)
            if(N//i>i):
                L.append(N//i)
    L=sorted(L)
    return L

N=int(input())
L=calc(N)
s=0
for num in L:
    if(num<=2):
        continue
    if(N//(num-1)==N%(num-1)):
        s+=(num-1)

print(s)
