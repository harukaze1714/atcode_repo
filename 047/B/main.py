W,H,N = map(int,input().split())
Xl=0
Xr=W
Yu=0
Yh=H

for i in range(N):
    Xt,Yt,At = map(int,input().split())
    if((At==1)and(Xl<Xt)):
        Xl=Xt
    elif((At==2)and(Xr>Xt)):
        Xr=Xt
    elif((At==3)and(Yu<Yt)):
        Yu=Yt
    elif((At==4)and(Yh>Yt)):
        Yh=Yt

if((Xr<=Xl)or(Yh<=Yu)):
    print("0")
else:
    print((Xr-Xl)*(Yh-Yu))