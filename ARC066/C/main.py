N = int(input())
A = list(map(int, input().split()))

A.sort()

if(N%2==0):
    for i in range(N//2):
        if((A[i*2]!=(1+i*2))|(A[2*i+1]!=(1+i*2))):
            print(0)
            exit()
    print((2**(N//2)) % int(1e9+7))

else:
    if(A[0]!=0):
            print(0)
            exit()
    for i in range(N//2):
        if((A[i*2+1]!=((i+1)*2))|(A[i*2+2]!=((i+1)*2))):
            print(0)
            exit()
    print((2**(N//2)) % int(1e9+7))
