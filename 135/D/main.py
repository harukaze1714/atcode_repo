cnt=0

def calcuration(i,A,B):
        global cnt
        if(A[i]=="?"):
                for k in range(10):
                        tmp=""
                        B[i]=k
                        if(i!=len(A)-1):
                                calcuration(i+1,A,B)
                        else:
                                for para2 in B:
                                        tmp+=str(para2)
                                tmp = int(tmp)
                                #print(tmp)
                                if(tmp%13==5):
                                        #print("OK")
                                        cnt+=1
        else:
                if(i!=len(A)-1):
                        calcuration(i+1,A,B)
                else:
                        tmp=""
                        for para2 in B:
                                tmp+=str(para2)
                        tmp = int(tmp)
                        #print(tmp)
                        if(tmp%13==5):
                                #print("OK")
                                cnt+=1


A = list(input())
B = A[:]

for num,para in enumerate(B):
    if(para=="?"):
        B[num]=0

calcuration(0,A,B)


print(cnt%(10**9+7))


