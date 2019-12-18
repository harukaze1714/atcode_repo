n = int(input())
a = [int(input()) for i in range(n)]

count=0

for i in range(n):
    if(a[i]>0):
        count+=(a[i]-1)//2
        a[i]=((a[i]-1))%2+1


for i in range(n-1):
    count+=a[i]//2
    a[i]=a[i]%2
    if((a[i]>0) & (a[i+1]>0)):
        MinNum=min(a[i],a[i+1])
        a[i]-=MinNum
        a[i+1]-=MinNum
        count = count+MinNum


count+=a[n-1]//2
a[n-1]=a[n-1]%2

print(count)