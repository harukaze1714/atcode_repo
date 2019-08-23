N,Y = map(int, input().split())

A=0
B=0
C=int(Y/1000)
i=0
for j in range(2*10**7):
    for i in range(C,-1,-5):
        if((A+B+i)==N):
            print(A,B,i)
            exit()
        B+=1
    if((A+B+i)==N):
            print(A,B,i)
            exit()
    A+=1
    C-=10
    B=0
    if((10*A+5*B+i)>(Y/1000)):
        print("-1 -1 -1")
        exit()
print(A,B,i)



