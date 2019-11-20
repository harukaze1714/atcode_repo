N = int(input())

List=[[0]*2 for i in range(N)]
for i in range(N):
    A,B=map(int,input().split())
    List[i][0]=A
    List[i][1]=B

List=sorted(List,key=lambda x: x[1])

total=0
for i in range(N):
    total+=List[i][0]
    if(total>List[i][1]):
        print("No")
        exit()
print("Yes")