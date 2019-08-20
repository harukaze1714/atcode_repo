H = list(input())
N = [1]*len(H)
T = N[:]
J0 = [2]*len(H)
J1 = [3]*len(H)
k=0
while True:
    k+=1

    if(J0==J1):break

    for i,para in enumerate(H):
        if(N[i]!=0):
            if(para=="R"):
                T[i+1]+=N[i]
            else:
                T[i-1]+=N[i]
            T[i]-=N[i]
    N=T[:]
    if(k%2==0):
        J1=J0[:]
        J0=N[:]

for para in N:
    print(para, end=" ")

