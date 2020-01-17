N=int(input())

if(N%2==1):
    print(0)
    exit()

#s=0
#for i in range(2,N+1,2):
#    while(i%5==0 and i!=0):
#        s+=1
#        i=i//5
#print(s)

s=0
t=10
while(N>=t):
    s+=(N//t)
    t*=5
print(s)

#L=len(str(N))-1
#s+=L*(L-1)
#T=N//10
#s+=T
#print(s)
