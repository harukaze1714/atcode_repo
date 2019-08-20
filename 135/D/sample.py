#117,104

A = list(input())
print(3625%13)

i = 0
tmp=int(A[i]+A[i+1])
for j in range(7, 0, -1):
    if(tmp<13*j):
        False
        #何もしない
    if(tmp>13*j):
        ans=tmp-13*j
        if(ans>10):
            A[i]=str(ans)[0]
            A[i+1]=str(ans)[1]
            break
        else:
            A[i]=str(0)
            A[i+1]=str(ans)[0]
            break

for i in range(len(A)-2):
    tmp=int(A[i]+A[i+1]+A[i+2])
    if(tmp>118):
        if(tmp>99):tmp=int(A[i]+A[i+1])
        for j in range(7, 0, -1):
            if(tmp<13*j):
                False
                #何もしない
            if(tmp>13*j):
                ans=tmp-13*j
                if(ans>10):
                    A[i]=str(ans)[0]
                    A[i+1]=str(ans)[1]
                    break
                else:
                    A[i]=0
                    A[i+1]=str(ans)[0]
                    break
    else:
        for j in range(9, 7, -1):
            if(tmp<13*j):
                False
                #何もしない
            if(tmp>13*j):
                ans=tmp-13*j
                if(ans>10):
                    A[i]=str(ans)[0]
                    A[i+1]=str(ans)[1]
                    break
                else:
                    A[i]=0
                    A[i+1]=str(ans)[0]
                    break

i = len(A)-2
tmp=int(A[i]+A[i+1])
for j in range(7, 0, -1):
    if(tmp<13*j):
        False
        #何もしない
    if(tmp>13*j):
        ans=tmp-13*j
        if(ans>10):
            A[i]=str(ans)[0]
            A[i+1]=str(ans)[1]
            break
        else:
            A[i]=0
            A[i+1]=str(ans)[0]
            break
print(A)


cnt=0

def calcuration(i,A,B):
        global cnt
        for j in range(i,len(A)):
                 if(para=="?"):
                        for i in range(10):
                                tmp=""
                                B[j]=i
                                calcuration(j,A,B)
                                for para2 in B:
                                        tmp+=str(para2)
                                tmp = int(tmp)
                                print(tmp)
                                if(tmp%13==5):
                                        print("OK")
                                        cnt+=1


A = list(input())
B = A[:]

for num,para in enumerate(B):
    if(para=="?"):
        B[num]=0

calcuration(0,A,B)

print("cnt:",cnt)


