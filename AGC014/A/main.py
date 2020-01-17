A,B,C=map(int,input().split())

t=0
while(True):
    if(A%2==1 or B%2==1 or C%2==1) :
        break
    a=(A+B)/2
    b=(B+C)/2
    c=(C+A)/2
    if(A==a and B==b and C==c):
        print(-1)
        exit()
    A=a
    B=b
    C=c
    t+=1
print(t)
