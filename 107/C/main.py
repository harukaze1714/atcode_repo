N,K=map(int,input().split())
A=list(map(int,input().split()))

f=0
s=0
t=N
for i in range(N):
    if(A[i]>=0):
        t=i
        break

M=A[0:t]
for i in range(len(M)):
    M[i]*=-1
M=sorted(M)

if(t==N):
    P=[]
elif(A[t]==0):
    P=A[t+1:N]
    s+=1
else:
    P=A[t:N]
M.append(10**10)
M.insert(0,0)
P.append(10**10)
P.insert(0,0)

t=s
m=1
p=1
a=0
while(True):
    if(t>=K):
        a=P[p-1]+(M[m-1]*2)
        break
    if(P[p]<=(M[m]*2)):
        p+=1
    else:
        m+=1
    t+=1

t=s
m=1
p=1
bin=0
while(True):
    if(t>=K):        
        b=(P[p-1]*2)+M[m-1]
        break
    if((P[p]*2)<=(M[m])):
        p+=1
    else:
        m+=1
    t+=1


print(min(a,b))

