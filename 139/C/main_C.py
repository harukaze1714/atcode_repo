S = int(input())
H = list(map(int, input().split()))

max=0
tmp=0

for i in range(len(H)-1):
    if(H[i]>=H[i+1]):
        tmp+=1
    else:
        if(max<tmp):
            max=tmp
        tmp=0
if(max<tmp):
    max=tmp

print(max)

