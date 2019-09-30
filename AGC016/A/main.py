S=input()
C=[0]*len(S)
for i in range(len(S)):
    if(S[0]!=S[i]):
        break
else:
    print(0)
    exit()

total=10**10
for i in range(len(S)):
    I=len(S)-i-1
    if(C[I]==0):
        #subtotal=I-1
        subtotal=0
        tmp=0
        for j in range(len(S)-i-1):
            J=I-j-1
            tmp+=1
            a=S[I]
            b=S[J]
            if(S[I]==S[J]):
                C[J]=1
                if(subtotal<tmp):
                    subtotal=tmp-1
                    tmp=0
        subtotal=max(tmp,i,subtotal)

        if(total>subtotal):
            total=subtotal
"""
        a=S[i]
        b=S[j]
        if(S[i]==S[j]):
            if(subtotal<tmp):
                subtotal=tmp
                tmp=0
            else:
                tmp+=1
        else:
            tmp+=1
    if(total>max(i,tmp+2)):
        total=max(i,tmp+2)
        print(a)

    if((total>subtotal)&(subtotal!=0)):
        total=subtotal
        print(a)
"""
print(total)
