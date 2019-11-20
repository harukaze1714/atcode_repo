S=list(input())

Dict={}
Dict["a"]=1
Dict["b"]=1
Dict["c"]=1
for i in range(len(S)):
    Dict[S[i]]+=1
if(("".join(S)=="aa")|("".join(S)=="bb")|("".join(S)=="cc")):
    print("NO")
    exit()

if(len(S)<3):
    print("YES")
    exit()

if((max(Dict.values())-min(Dict.values()))>1):
    print("NO")
else:
    print("YES")  