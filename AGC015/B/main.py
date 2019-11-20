S=input()
N=len(S)

total=0
for i in range(N):
    if(S[i]=="U"):
        total+=N-1-i
        total+=i*2
    else:
        total+=i
        total+=(N-1-i)*2

print(total)