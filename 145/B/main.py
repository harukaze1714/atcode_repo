N=int(input())
S=input()
S1=S[0:N//2]
S2=S[N//2:N]

if(S1==S2):
    print("Yes")
else:
    print("No")