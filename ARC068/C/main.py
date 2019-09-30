X = int(input())

N=((X-1)//11)*2
P=(X-1)%11

if(P>5):
    print(N+2)
else:
    print(N+1)