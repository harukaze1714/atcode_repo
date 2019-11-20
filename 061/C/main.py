N,K =map(int,input().split())

LIST=[[0,0] for i in range(N)]

for i in range(N):
    LIST[i][0],LIST[i][1]=map(int,input().split())

LIST=sorted(LIST)

c=0
for i in range(N):
    c+=LIST[i][1]
    if(c>=K):
        print(LIST[i][0])
        exit()

