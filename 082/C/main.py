N = int(input())
A = list(map(int,input().split()))

Dic={}
for i in A:
    if Dic.get(i,None)==None:
        Dic[i]=1
    else:
        Dic[i]+=1
total=0
for i,j in Dic.items():
    if i <= j:
        total+=j-i
    else :
        total+=j
print(total)

