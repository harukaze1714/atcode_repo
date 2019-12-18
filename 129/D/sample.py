#H=4
#W=6
#
#S[0]=["#",".",".","#",".","."]
#S[1]=[".",".",".",".",".","#"]
#S[2]=[".",".",".",".","#","."]
#S[3]=["#",".","#",".",".","."]

H,W=map(int,input().split())
S=[0]*H
for i in range(H):
    S[i]=list(input())


MAP=[[[0,0,0,0] for i in range(W)]for i in range(H)]
#MAP[H][W]

#ue
for i in range(W):
    c=0
    for j in range(H):
        if(S[j][i]=="."):
            c+=1
            MAP[j][i][0]=c
        else:
            c=0
            MAP[j][i][0]=c

#shita
for i in range(W):
    c=0
    for j in range(H-1,-1,-1):
        if(S[j][i]=="."):
            c+=1
            MAP[j][i][1]=c
        else:
            c=0
            MAP[j][i][1]=c

#hidari
for j in range(H):
    c=0
    for i in range(W):
        if(S[j][i]=="."):
            c+=1
            MAP[j][i][2]=c
        else:
            c=0
            MAP[j][i][2]=c

#migi
for j in range(H):
    c=0
    for i in range(W-1,-1,-1):
        if(S[j][i]=="."):
            c+=1
            MAP[j][i][3]=c
        else:
            c=0
            MAP[j][i][3]=c

MAX=0
for i in range(W):
    for j in range(H):
        t=0
        t+=MAP[j][i][0]
        t+=MAP[j][i][1]
        t+=MAP[j][i][2]
        t+=MAP[j][i][3]  
        t-=3              
        MAX=max(MAX,t)
print(MAX)