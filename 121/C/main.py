S=input()

total=0
count=0
for i in range(len(S)):
    if(int(S[i])==1):
        p=1
    else:
        p=-1
    if(total*p<0):
        count+=1
    total+=p

print(count*2)