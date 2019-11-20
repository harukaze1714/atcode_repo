S=input()
Dict={}

for s in range(len(S)):
    if(Dict.get(S[s],None)==None):
        Dict[S[s]]=1
    else:
        Dict[S[s]]+=1
MIN=10*10

for s in Dict:
    count=0
    tMAX=0
    for s2 in range(len(S)):
        if(S[s2]==s):
            tMAX=max(tMAX,count)
            count=0
        else:
            count+=1
    tMAX=max(tMAX,count)    
    MIN=min(MIN,tMAX)

print(MIN)

