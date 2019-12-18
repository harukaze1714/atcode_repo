N=int(input())
S=input()

D=[0]*100
C=0
W=[0]*10
R=len(set(S))**3
u=0
for i in range(N-2):
    if(C==R):
        break
    if(W[int(S[i])]<10):
        u=len(set(S[i+1:N]))
        for j in range(i+1,N-1):
            if(W[int(S[i])]==u):
                break
            s=str(S[i])+str(S[j])
            if(D[int(s)]==0):
                D[int(s)]=1
                W[int(S[i])]+=1
                C+=len(set(S[j+1:N]))
print(C)

