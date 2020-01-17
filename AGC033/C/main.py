H,W=map(int,input().split())

MAP=[["." for i in range (W)]for i in range(H)]
LIST=[0]*(10**6+100)

l=0
r=0
for i in range(H):
    A=list(input())
    for j in range(W):
        if(A[j]=="#"):
            MAP[i][j]="#"
            LIST[r]=(i,j,0)
            r+=1

while(True):
    T=LIST[l]
    i=T[0]
    j=T[1]
    if(i>0):
        if(MAP[i-1][j]=="."):
            MAP[i-1][j]="#"
            LIST[r]=(i-1,j,T[2]+1)
            r+=1  
    if(i+1<H):
        if(MAP[i+1][j]=="."):
            MAP[i+1][j]="#"
            LIST[r]=(i+1,j,T[2]+1)
            r+=1  
    if(j>0):
        if(MAP[i][j-1]=="."):
            MAP[i][j-1]="#"
            LIST[r]=(i,j-1,T[2]+1)
            r+=1  
    if(j+1<W):
        if(MAP[i][j+1]=="."):
            MAP[i][j+1]="#"
            LIST[r]=(i,j+1,T[2]+1)
            r+=1
    l+=1
    if(r<=l):
        print(LIST[r-1][2])
        exit()  

