N,C,K=map(int,input().split())
A=[0]*N

for i in range(N):
    A[i]=int(input())
A=sorted(A,reverse=True)

IND=0
total=0
while(len(A)>0):
    total+=1
    IND=A[0]-K
    count=0
    i=0
    while((len(A)>0)&(count<C)) :
        if(A[0]<IND):break
        A.pop(0)
        count+=1
print(total)