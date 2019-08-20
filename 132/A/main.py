d={}
A = input()
for i in range(len(A)):
    if d.get(A[i],None)==None:
        d[A[i]]=1
    else:
        d[A[i]]+=1

if(max(d.values())==2 & min(d.values())==2):
    print("Yes")
else:print("No")