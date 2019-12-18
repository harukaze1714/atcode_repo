H,W=map(int,input().split())

M=["."]*H
C=[[0]*50 for i in range(50)]
L=[[0,0,0] for i in range(10**5)]

s=0
for i in range(H):
    t=list(input())
    s+=t.count("#")
    M[i]=t

c=0
i=0
p=0
while(True):
    x=L[i][0]
    y=L[i][1]
    p=L[i][2]
    if(i>c):
        print(-1)
        break
    
    if((H-1)==y and (W-1)==x):
        print(H*W-s-p-1)
        exit()

    if(y>0):
        if(M[y-1][x]=="." and C[y-1][x]==0):    
            c+=1
            L[c][0]=x
            L[c][1]=y-1
            L[c][2]=p+1
            C[y-1][x]=1
    if(x<(W-1)):
        if(M[y][x+1]=="." and C[y][x+1]==0):
            c+=1
            L[c][0]=x+1
            L[c][1]=y
            L[c][2]=p+1
            C[y][x+1]=1
    if(y<(H-1)):
        if(M[y+1][x]=="." and C[y+1][x]==0):
            c+=1
            L[c][0]=x
            L[c][1]=y+1
            L[c][2]=p+1
            C[y+1][x]=1
    if(x>0):
       if(M[y][x-1]=="." and C[y][x-1]==0):
            c+=1
            L[c][0]=x-1
            L[c][1]=y
            L[c][2]=p+1
            C[y][x-1]=1
    i+=1
