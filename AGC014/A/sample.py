So=list(input())
S=So
C=[0]*len(S)
for i in range(len(S)):
    if(S[0]!=S[i]):
        break
else:
    print(0)
    exit()

for i in range(len(S)):
    for k in range(len(S)):
        S[k]=So[k]

    count=0
    flag=0
    while(True):
        count+=1
        print(S)
        i=0
        for j in range(i+1,len(S)):
            if(S[i]==S[j]):
                S[j-1]=S[i]
                end=j
        S.pop(len(S)-1)
        frag=1
        for k in range(len(S)):
            if(S[0]!=S[k]):
                frag=0
                break
        if((len(S)==0)|frag==1):
            break
    print(S)
    print(count)