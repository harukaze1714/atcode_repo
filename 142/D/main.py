def number(a):
    MAX=int(a**0.5)+1
    l=[]
    for i in range(1,MAX):
        if(a%i==0):
            l.append(i)
            if(i != a//i):
                l.append(a//i)
    l=sorted(l)
    return l

def check(c,t):
    for i in c:
        if(t%i==0):
            if(i!=1):
                return False
    
    return True


A,B=map(int,input().split())

listA=number(A)
listB=number(B)
a=0
b=0
c=[]
while(True):
    if(listA[a]==listB[b]):
        if(check(c,listA[a])):
            c.append(listA[a])
        a+=1
        b+=1
    elif(listA[a]>listB[b]):
        b+=1
    else:
        a+=1
    if(len(listA)==a or len(listB)==b):
        print(len(c))
        exit()  