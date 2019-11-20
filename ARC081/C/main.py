N = int(input())
A = list(map(int, input().split()))

Dict={}
for i in A:
    if(Dict.get(i,None)==None):
        Dict[i]=1
    else:
        Dict[i]+=1

T=1
C=0
Dict = sorted(Dict.items(), key=lambda x:-x[0])
for i in Dict:
    if((i[1]>=2)&(C>=1)):
        T*=i[0]
        C+=1
        break
    if(i[1]>=4):
        T*=i[0]*i[0]
        C=2
        break
    if(i[1]>=2):
        T*=i[0]
        C+=1

if(C==2):
    print(T)
else:
    print("0")
    