N,M=map(int,input().split())
T=list(map(int,input().split()))
#N=9999 
#M=1
#T=[1,3,4,5,6,7,8,9]
#T=[]
L=[]
for i in range(10):
    if(not T.count(i)):
        L.append(i)

l=len(str(N))+1
MIN=10**10

def calc(st):
    global MIN
    st=str(st)
    if(len(st)>l):return 0
    for num in L:
        t=calc(st+str(num))
        if(int(t)>=N):
            MIN=min(MIN,int(t))
    if(st!=""):
        if(int(st)>=N):
            MIN=min(int(st),MIN)
    return (MIN)

print(calc(str()))





