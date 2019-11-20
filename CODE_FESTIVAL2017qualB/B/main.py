N=int(input())
D = list(map(int, input().split()))
M=int(input())
T = list(map(int, input().split()))


List = {}
for i in D:
    if List.get(i,None)==None:
        List[i]=1
    else:
        List[i]+=1


for i in T:
    if List.get(i,None)==None:
        print("NO")
        exit()
    else:
        if(List[i]==1):
            del List[i]
        else:
            List[i]-=1
        

print("YES")