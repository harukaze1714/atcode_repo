N , K = map(int, input().split())
S = list(input())
gap=0
for i in range(N-1):
    if(S[i]!=S[i+1]):
        gap+=1

P=len(S)-1-gap
if(gap==0):
    print(P)
    exit()

for i in range(K):
    if(gap>1):
        P+=2
    else:
        P+=1
        break
    gap-=2
    if(gap==0):
        break

print(P)