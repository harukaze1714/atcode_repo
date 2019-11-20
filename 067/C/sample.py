S = input()
T = input()
lenS=len(S)
lenT=len(T)
ans=["a"]*lenS
for i in range (lenS):
    if(S[i]!="?"):
        ans[i]=S[i]
flag=0
for j in range(lenS-lenT+1):
    flag=1
    for i in range (lenS):
        if(S[i]=="?"):
            ans[i]="a"

    for i in range(1,lenT+1):
        if((S[lenS-i-j]!="?")&(S[lenS-i-j]!=T[lenT-i])):
            flag=0
            break
        else:
            ans[lenS-i-j]=T[lenT-i]
    
    if(flag==1):
        break

if(flag==1):
    print("".join(ans))
else:
    print("UNRESTORABLE")

    