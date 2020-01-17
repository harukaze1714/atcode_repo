N = int(input())
#N=44852
LIST=[10**9]*(10**7)
LIST[0]=1

i=1
c=1
while(6**i <= N):
    LIST[c]=6**i
    c+=1
    if(9**i <= N):
        LIST[c]=9**i
        c+=1
    i+=1
LIST=LIST[0:c]
LIST=list(sorted(LIST,reverse=True))
MIN=10**10

def calc(L,i,c):
    global MIN
    global N
    if(MIN<c):
        return
    if(N-L >= LIST[i]):
        calc(L+LIST[i],i,c+1)
        if(MIN<c):
            return
    if(len(LIST)-2>=i):
        calc(L,i+1,c)
        if(MIN<c):
            return
    if(N==L):
        MIN=min(MIN,c)
  

calc(0,0,0)
print(MIN)