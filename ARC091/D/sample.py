#N,K=map(int,input().split())
N=352
K=54
LIST=[]
LIST2=[]
s=0

for i in range(1,N+1):
    for j in range(1,N+1):
        if i%j >= K:
            LIST2.append((i,j))
            s+=1

print(s)
