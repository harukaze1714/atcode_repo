A,B,X=map(int,input().split())
N=10**9
i=0
if(X>=((A*N)+(B*len(str(N))))):
    print(N)
    exit()
S=0
T=0

while(True):
    T=S+(N//2)
    N=N//2
    Q=((A*T)+(B*len(str(T))))
    if(X<Q):
        T=S
    S=T
    if(N==0):break

if(T==0):
    print("0")
    exit()

for i in range(S,10**10):
    if(X>=((A*i)+(B*len(str(i))))):
        if(X<((A*(i+1))+(B*len(str(i+1))))):
            print(i)
            exit()
