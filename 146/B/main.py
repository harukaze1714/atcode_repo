N=int(input())
S=input()
M="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"


for i in range(len(S)):
    for j in range(26):
        if S[i]==M[j] :
            print(M[j+N],end="")