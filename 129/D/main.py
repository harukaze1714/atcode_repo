#H=4
#W=6
#
#S[0]=["#",".",".","#",".","."]
#S[1]=[".",".",".",".",".","#"]
#S[2]=[".",".",".",".","#","."]
#S[3]=["#",".","#",".",".","."]

H,W = map(int,input().split())

S = [[0]*W for i in range(H)]

for i in range(H):
    T=list(input())
    for j in range(W):
        if T[j] == "#":
            S[i][j] = 0
        else:
            S[i][j] = 1
MAP=[[0]*(W+2) for i in range(H+2)]
MAPH=[[0]*(W+2) for i in range(H+2)]
MAPU=[[0]*(W+2) for i in range(H+2)]
MAPL=[[0]*(W+2) for i in range(H+2)]
MAPR=[[0]*(W+2) for i in range(H+2)]

MAX=0
for i in range(1,W+1):
    for j in range(1,H+1):
            MAPH[j][i]=(MAPH[j-1][i]+1)*S[j-1][i-1]
            MAP[j][i]+=MAPH[j][i]
            MAPU[H-j+1][W-i+1]=(MAPU[H-j+2][W-i+1]+1)*S[H-j][W-i]
            MAP[H-j+1][W-i+1]+=MAPU[H-j+1][W-i+1]
for j in range(1,H+1):
    for i in range(1,W+1):
            MAPL[j][i]=(MAPL[j][i-1]+1)*S[j-1][i-1]
            MAP[j][i]+=MAPL[j][i]
            MAPR[H-j+1][W-i+1]=(MAPR[H-j+1][W-i+2]+1)*S[H-j][W-i]
            MAP[H-j+1][W-i+1]+=MAPR[H-j+1][W-i+1]
            MAX=max(MAX,MAP[j][i]-3,MAP[H-j+1][W-i+1]-3)
print(MAX)