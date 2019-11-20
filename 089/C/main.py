N = int(input())
Dict={}
for i in range(N):
    T=input()
    if Dict.get(T[0],None)==None:
        Dict[T[0]]=1
    else:
        Dict[T[0]]+=1

L=[]
if Dict.get("M",None)!=None:
    L.append(Dict["M"])
if Dict.get("R",None)!=None:
    L.append(Dict["R"])
if Dict.get("A",None)!=None:
    L.append(Dict["A"])
if Dict.get("C",None)!=None:
    L.append(Dict["C"])
if Dict.get("H",None)!=None:
    L.append(Dict["H"])
if(len(L)<3):
    print(0)
    exit()


S=0
for i in range(len(L)):
    for j in range(len(L)):
        if(i==j):break
        for k in range(len(L)):
            if(i==k):break
            if(j==k):break
            S+=L[i]*L[j]*L[k]
print(S)