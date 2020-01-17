N=int(input())
A=[0]*N    

for i in range(N):
    A[i]=list(map(int,input().split()))
A=sorted(A,key=lambda x: (x[0],x[1]))

"""
if(N==1):
    print(A[0][0],A[0][1],A[0][2])
    exit()
H=0
x=0
y=0
for i in range(101):
    for j in range(101):
        f=0
        h=abs(i-A[0][0])+abs(j-A[0][1])+A[0][2]
        for k in range(N):
            if(h!=abs(i-A[k][0])+abs(j-A[k][1])+A[k][2]):
                f=1
                break 
        if(f==0):
            if(h>H):
                H=h
                x=i
                y=j
print(x,y,H)
"""
for cx in range(101):
    for cy in range(101):
        flag=True
        Hcand=-1
        for x,y,h in A:
            if h==0 and H>0:
                if H-abs(x-cx)-abs(y-cy)>0:
                    flag=False
                    break
            else:
                H= h+abs(x-cx)+abs(y-cy)
                if Hcand==-1:
                    Hcand=H
                else:
                    if Hcand!=H:
                        flag=False
                        break
        if flag:
            break
    if flag:
        break
print(cx,cy,H)
