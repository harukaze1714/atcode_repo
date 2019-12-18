H,W,K=map(int,input().split())

M=[[0 for i in range(W)] for f in range(H)]
A=[[0 for i in range(W)] for f in range(H)]

for i in range(H):
    M[i]=list(input())

f=1
s=1
for i in range(W):
    c=0
    for j in range(H):
        if(M[j][i]=="#"):
            c+=1
    if(c==0):
        f+=1
    else:
        t=0
        for j in range(H):
            if(M[j][i]=="#"):
                t+=1
                if(t>1):
                    s+=1     
            for k in range(f):
                A[j][i-k]=s
        f=1
        s+=1


for i in range(W-1,-1,-1):
    if(A[0][i]!=0):
        for j in range(i,W):
            for k in range(H):
                A[k][j]=A[k][i]
        break

for i in range(H):
    for j in range(W):
        print(A[i][j],end=" ")
    print()