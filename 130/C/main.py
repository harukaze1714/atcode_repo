W,H,x,y = map(int, input().split())

"""
A=min(W-x,x)*H
B=min(H-y,y)*W

if(A==B):
    print(A,"1")
else:
    print(max(A,B),"0")

"""
ans=W*H/2
if((W/2==x) & (H/2==y)):
    print(ans,"1")
else:
    print(ans,"0")
