A,B,X=map(int,input().split())

i=0
N=0
while(True):
    N=N*10+9
    i+=1
    if((N*A+i*B)>=X):
        break
    if(N>(10**10)):
        break

for j in range(N,-1,-1):
    if((j*A+i*B)<=X):
        print(j)
        exit()
print("0")
    