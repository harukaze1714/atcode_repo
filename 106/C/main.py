S=input()
K=int(input())

T=5*(10**15)
t=0
for s in S:
    if(s=="1"):
        t+=1
        if(t==K):
            print(1)
            exit()
    else:
        print(s)
        exit()