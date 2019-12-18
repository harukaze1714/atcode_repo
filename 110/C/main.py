S=input()
T=input()
S2=[0]*len(S)
T2=[0]*len(T)
SD={}
TD={}

c=0
for i in range(len(S)):
    if(SD.get(S[i],None)==None):
        c+=1
        SD[S[i]]=c
        S2[i]=c
    else:
        S2[i]=SD.get(S[i],None)
c=0
for i in range(len(T)):
    if(TD.get(T[i],None)==None):
        c+=1
        TD[T[i]]=c
        T2[i]=c
    else:
        T2[i]=TD.get(T[i],None)
if(S2==T2):
    print("Yes")
else:
    print("No")


