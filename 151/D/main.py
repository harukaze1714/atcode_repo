H,W=map(int,input().split())
MAP=[0]*H
for i in range(H):
    MAP[i]=list(input())

def calc(x,y):
    CMAP=[[0 for i in range(W)]for i in range(H)]
    LIST=[0 for i in range (3)]*10**4
    t=1
    k=0
    c=0
    LIST[0]=[x,y,c]
    while(True):
        x=LIST[k][0]
        y=LIST[k][1]
        c=LIST[k][2]
        if(x>0):
            if(CMAP[y][x-1]==0 and MAP[y][x-1]=="."):
                CMAP[y][x-1]=1
                LIST[t]=[x-1,y,c+1]
                t+=1
        if(y>0):
            if(CMAP[y-1][x]==0 and MAP[y-1][x]=="."):
                CMAP[y-1][x]=1
                LIST[t]=[x,y-1,c+1]
                t+=1
        if(x<W-1):
            if(CMAP[y][x+1]==0 and MAP[y][x+1]=="."):
                CMAP[y][x+1]=1
                LIST[t]=[x+1,y,c+1]
                t+=1
        if(y<H-1):    
            if(CMAP[y+1][x]==0 and MAP[y+1][x]=="."):
                CMAP[y+1][x]=1
                LIST[t]=[x,y+1,c+1]
                t+=1
        k+=1
        if(k==t):break
    return c

m=0
for i in range(H):
    for j in range(W):
        if MAP[i][j]=="." :
            m=max(m,calc(j,i))

print(m)

