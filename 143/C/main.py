N=int(input())
S=input()

t=1
for i in range(N-1):
    if(S[i]!=S[i+1]):
        t+=1

print(t)
