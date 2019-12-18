S=input()
s=0
c=0
for i in range(len(S)):
    if("S"==S[i]):
        s+=1
    else:
        if(s>0):
            s-=1
            c+=1

if(c>10**5):
    print(len(S)-(2*(10**5)))
else:
    print(len(S)-(2*c))