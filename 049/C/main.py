S=input()
lenS=len(S)
L=[0]*10000
j=0
i=0
s=0
S+="######################"
while(True):
    if(lenS==i):
        print("YES")
        exit()
    if(S[i:i+7]=="dreamer" and s<1):
        L[j]=1
        j+=1
        i+=7
        s=0
        continue
    if(S[i:i+5]=="dream" and s<2):
        L[j]=2
        j+=1
        i+=5
        s=0
        continue
    if(S[i:i+6]=="eraser" and s<3):
        L[j]=3
        j+=1
        i+=6
        s=0
        continue
    if(S[i:i+5]=="erase" and s<4):
        L[j]=4
        j+=1
        i+=5
        s=0
        continue
    j-=1
    if(j<0):
        print("NO")
        exit()
    if(L[j]==1):
        i-=7
        s=1
    elif(L[j]==2):
        i-=5
        s=2
    elif(L[j]==3):
        i-=6
        s=3    
    elif(L[j]==4):
        i-=5
        s=4




