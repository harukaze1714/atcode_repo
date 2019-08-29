N,K=map(int,input().split())
if K%2==1:
    s=N//K
    print(s**3)
    exit()
k=K//2
s=N//k
num=0
if s%2==0:
    print((s**3)//4)
    exit()
t=((s//2+1)**2)*(s//2+1)
u=((s//2)**2)*(s//2)
print(t+u)