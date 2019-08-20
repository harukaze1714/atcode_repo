N = int(input())
strN = str(N)
#print(N)
sum=0

if(len(strN)%2==1):
    sum+=N-10**(len(strN)-1)+1
    #print(sum)

for i in range(len(strN)-1,0,-1):
    #print(i)
    if(i%2==1):
        sum+=10**(i-1)*9
        #print(sum)
if(len(strN)==1):
    sum=N

print(sum)


