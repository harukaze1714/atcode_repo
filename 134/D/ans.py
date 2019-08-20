import math
 
n=int(input())
alist=list(map(int, input().split())) 
blist=[]
for i in range(n):
    blist.append([])
 
for i in range(n):
    ima=n-i-1
    kosu=math.floor(n/(ima+1))
    nanko=0
    #print(ima, kosu)
    for j in range(kosu-1):
        #nima=(kosu-j-1)*(ima+1)
        nima=(ima+1)*(kosu-j)-1
        #print(nima)
        if blist[nima][0]==1:
            nanko+=1
    nanko=nanko%2
    if alist[ima]==nanko:
        blist[ima]=[0]
    else:
        blist[ima]=[1]
 
#print(blist)
kotaelist=[]
for bl in range(n):
    if blist[bl]==[1]:
        kotaelist.append(bl+1)
 
print(len(kotaelist))
for s in kotaelist:
    print(s, end =" ")