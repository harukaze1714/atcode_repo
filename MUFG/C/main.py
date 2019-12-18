X=int(input())

x=X%100
C=X//100

c=0
while(True):
    if(x>=5):
        x-=5
    else:
        x=0
    c+=1
    if(x==0):
        if(C>=c):
            print(1)
            exit()
        else:
            print(0)
            exit()
