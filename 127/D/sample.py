N,M=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)
BC=[[0,0] for i in range(M)]
for i in range(M):
    BC[i][0],BC[i][1]=map(int,input().split())
BC=list(sorted(BC,reverse=True,key=lambda x: x[1]))

c=0
for i in range(M):
    c=1
    for j in range(BC[i][0]):
        if(BC[i][1]>=A[j]):
            A[j]=BC[i][1]
            c=0
        else:
            break
    if(c==0):
        A=sorted(A)
    else:
        break

print(sum(A))