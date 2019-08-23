def one(L,param,num):
    tmp=0
    if(len(param)!=0):
        if(param[0]=="0"):
            num+="1"
            tmp=one(L,param[1:len(param)],num)
            if(tmp!=0):return tmp
        else:
            num+="0"
            tmp=one(L,param[1:len(param)],num)
            if(tmp!=0):return tmp
            num=num[0:len(num)-1]
            num+="1"
            tmp=one(L,param[1:len(param)],num)
            if(tmp!=0):return tmp
    else:
        if(L.count(int(num,2))!=0):
            return int(num,2)
        else:
            return 0
    return 0    

N = int(input())
L = list(map(int, input().split()))

L.sort

MAX=max(L)
if(N%3!=0):
    if(MAX==0):
        print("Yes")
        exit()
    print("No")
    exit()

if((L.count(MAX)==(N/3))&(L.count(0)==(2*N/3))):
    print("Yes")
    exit()

K=len(str(format(max(L), 'b')))
L2=[0]*len(L)
for i in range(N):    
    tmp2=""
    tmp=str(format(L[i], 'b'))
    for j in range(K-len(tmp)):
        tmp2+="0"
    tmp2+=tmp
    L2[i]=tmp2
L3=[]
for i in range(2):
    num=one(L,L2[i],"")
    if(num==0) :
        print("No")
        exit()
    L.remove(num)
    L3.append(num)

t=0
while(True):
    if(len(L)==0):
        break
    tmp=int(bin(L3[i] ^ L3[i+1]),2)
    if(L.count(tmp)==0):
        print("No")
        exit()
    else:
        L.remove(tmp)
        L3.append(tmp)
    t+=1

print("Yes")