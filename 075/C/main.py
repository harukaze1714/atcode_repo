N,M=map(int,input().split())

MAP=[[0]*N for i in range(N)]
S=[0]*N
for i in range(M):
    a,b=map(int,input().split())
    MAP[a-1][b-1]+=1
    MAP[b-1][a-1]+=1
    S[a-1]+=1
    S[b-1]+=1

c=-1
s=0
while(True):
    c+=1
    if(c==N):
        break
    if S[c] == 1 :
        for i in range(N):
            if MAP[c][i] == 1 :
                MAP[c][i] = 0
                MAP[i][c] = 0
                S[c]-=1
                S[i]-=1
                s+=1
                c=-1
                break

print(s)
