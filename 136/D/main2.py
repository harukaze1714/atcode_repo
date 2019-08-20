H = list(input())
N = [0]*len(H)

Lflag=0
Rcnt=0
Lcnt=0
cnt=0
for i in range(1,len(H)+1):
    if((H[i-1]=="L") & (Lflag==0)):
        Lflag=1
        Rcnt=i-1
        Lcnt=i
    if((H[i-1]=="R") & (Lflag==1)):
        if((i-1-cnt)%2==0):
            N[Rcnt-1]=int(((i-1)-cnt)/2)
            N[Lcnt-1]=int(((i-1)-cnt)/2)

        else:
            if(Rcnt%2==(i-1)%2):
                N[Rcnt-1]=int(((i-1)-cnt)/2+1)
                N[Lcnt-1]=int(((i-1)-cnt)/2)
            else:
                N[Rcnt-1]=int(((i-1)-cnt)/2)
                N[Lcnt-1]=int(((i-1)-cnt)/2+1)
        cnt=i-1
        Lflag=0

if((len(H)-cnt)%2==0):
    N[Rcnt-1]=int((len(H)-cnt)/2)
    N[Lcnt-1]=int((len(H)-cnt)/2)

else:
    if(Rcnt%2==len(H)%2):
        N[Rcnt-1]=int((len(H)-cnt)/2+1)
        N[Lcnt-1]=int((len(H)-cnt)/2)
    else:
        N[Rcnt-1]=int((len(H)-cnt)/2)
        N[Lcnt-1]=int((len(H)-cnt)/2+1)
    
for para in N:
    print(para, end=" ")
