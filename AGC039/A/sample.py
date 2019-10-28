S = list(input())
K = int(input())
S2=S[:]+S[:]
S3=S[:]+S[:]+S[:]
count=0
for i in range(len(S)-1):
    if(S[i]==S[i+1]):
        S[i+1]="#"
        count+=1
count2=0
for i in range(len(S2)-1):
    if(S2[i]==S2[i+1]):
        S2[i+1]="#"
        count2+=1
count3=0
for i in range(len(S3)-1):
    if(S3[i]==S3[i+1]):
        S3[i+1]="#"
        count3+=1
#print(S)
N=count3-count2
E=count2-N

flag=0
if(S[0]==S[len(S)-1]):
    flag=1

if(flag==0):
    print(count*K)
else:
    if(K==1):
        print(count)
    else:
        print(N*(K-1)+E)



