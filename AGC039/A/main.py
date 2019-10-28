S = list(input())
K = int(input())
H=S[0]

flag=0
if(S[0]==S[len(S)-1]):
    flag=1
count=0
if(flag==0):
    for i in range(len(S)-1):
        if(S[i]==S[i+1]):
            S[i+1]="#"
            count+=1        
    print(count*K)
    exit()

flag2=0
for i in range(len(S)-1):
    if(S[i]!=S[i+1]):
        flag2=1
if(flag2==0):
    print((len(S)*K)//2)
    exit()

S1=S[:]
S2=S[:]+S[:]

count1=0
for i in range(len(S1)-1):
    if(S1[i]==S1[i+1]):
        S1[i+1]="#"
        count1+=1
count2=0
for i in range(len(S2)-1):
    if(S2[i]==S2[i+1]):
        S2[i+1]="#"
        count2+=1

print(count1+(K-1)*(count2-count1))