N,M=map(int,input().split())
A=list(map(int,input().split()))
BC=[[0,0] for i in range(M)]
for i in range(M):
    BC[i][0],BC[i][1]=map(int,input().split())

A=sorted(A)
BC=list(sorted(BC,reverse=True,key=lambda x: x[1]))

i=0
for B,C in BC:
    for j in range(i,min(N,i + B)):
        if A[j] < C:
            A[j] = C
            #B枚分先を飛ばす BCはCに関して降順のため問題ない
    i = i + B
 
print(sum(A))