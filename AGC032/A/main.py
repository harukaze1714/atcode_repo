N=int(input())
S=list(map(int,input().split()))
LIST=list("")

for i in range(N):
    if((S[i] - i)>1):
        print("-1")
        exit()  

while(len(S)>0):
    c=10**10
    for i in range (len(S)):
        if(S[i]==i+1):
            c=i
    if(c==(10**10)):
        print("-1")
        exit()  
    LIST.append(S.pop(c))

for i in range(len(LIST)-1,-1,-1):
    print(LIST[i])