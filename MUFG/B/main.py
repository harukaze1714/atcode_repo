A=int(input())
B=(A*100)//108

if((((B*1.08)//1)==A)):
    print(B)
elif((((B+1)*1.08)//1)==A):
    print(B+1)
else:
    print(":(")