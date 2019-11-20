N=int(input())
A = list(map(int, input().split()))

odd=0
even=0
even2=0

for num in A:
    if(num%2==1):
        odd+=1
    elif(num%4==0):
        even2+=1
    else:
        even+=1

if(even2>=odd):
    print("Yes")
elif((even==0)&(even2==(odd-1))):
    print("Yes")
else:
    print("No")