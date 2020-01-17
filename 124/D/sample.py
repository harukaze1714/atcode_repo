import sys
sys.setrecursionlimit(10 ** 9)
N,K=map(int,input().split())
S=input()

#N=14
#K=2
#S="11101010110011"

LIST=[[[0] for j in range (2)]for i in range(N)]

t=S[0]
c=0
k=0
for i in range(N):
    if(t!=S[i]):
        LIST[k][0]=c
        LIST[k][1]=t
        t=S[i]
        k+=1
        c=0
    c+=1

LIST[k][0]=c
LIST[k][1]=t
LIST=LIST[0:k+1]
MAX=0

def calc(i,s,K,f):
    global MAX
    MAX=max(MAX,s)
    if(i==len(LIST)):
        return

    if(LIST[i][1]=="1"):
        s+=LIST[i][0]
        MAX=max(MAX,s)
        i+=1
        if(i==len(LIST)):
            return
    if(K==0):
        return
    if(K>=1):
        calc(i+1,s+LIST[i][0],K-1,1)
    if(f==0):
        calc(i+1,0,K,0)

calc(0,0,K,0)
print(MAX)
