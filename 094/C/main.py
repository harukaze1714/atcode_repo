N = int(input())
A = list(map(int, input().split()))

Dict={}

for i,Num in enumerate(A):
    Dict[i]=Num

List = sorted(Dict.items(), key=lambda x:x[1])
S=List[(N//2)-1][1]
B=List[(N//2)][1]
for i in range(N):
    if(Dict[i]<=S):
        print(B)
    else:
        print(S)

