N=int(input())
S=list(input())

L=0
R=0

for i in range(N):
    if(S[i]=="("):
        R+=1
 
    elif(S[i]==")"):
        if(R==0):
            L+=1
        else:
            R-=1

for i in range(R):
        S.append(")")

for i in range(L):
    S.insert(0,"(")
    
print("".join(S))
