LIST=""
LIST=list(LIST)
c=0

def func(S):
    global LIST
    global c

    if(len(S)==0):
        c=1
    if(c==1):
        for i in range(len(LIST)-1,-1,-1):
            print(LIST[i])
        exit()

    So=S[::]
    for i in range(len(S)):
        S=So[::]
        if(S[i]==(i+1)):
            LIST.append(S.pop(i))
            func(S)
    if(len(LIST)==0):
        print("-1")
        exit()
    LIST.pop(-1)

N=int(input())
S=list(map(int,input().split()))

for i in range(N):
    if((S[i] - i)>1):
        print("-1")
        exit()  

func(S)
print("-1")