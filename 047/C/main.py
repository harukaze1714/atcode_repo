S=list(input())

T=S[0]
c=0

for s in S:
    if(T!=s):
        c+=1
        T=s
print(c)