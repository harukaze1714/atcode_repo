N=int(input())

total=0
for i in range(1,10**10):
    total+=i
    if(total>=N):
        print(i)
        exit()

