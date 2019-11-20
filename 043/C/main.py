N , M = map(int, input().split())

L=[[0]*2 for i in range(M)]

for i in range(M):
    L[i][0] , L[i][1] = map(int, input().split())

A=[0]*M
B=[0]*M

L=sorted(L ,key=lambda x: x[0])

for i in range(M):
    if L[i][0] == 1:
        A[i]=L[i][1]
    else:
        break
A=A[0:i]

L=sorted(L ,key=lambda x: -x[1])

for i in range(M):
    if L[i][1] == N:
        B[i]=L[i][0]
    else:
        break
B=B[0:i]

if((len(A)==0)or(len(B)==0)):
    print("IMPOSSIBLE")
    exit()
if((max(A)<min(B))or(max(B)<min(A))):
    print("IMPOSSIBLE")
    exit()

A.sort()
B.sort()
i=0
j=0
while((i<len(A))and(j<len(B))):
    if A[i] == B[j]:
        print("POSSIBLE")
        exit()
    elif A[i] > B[j]:j+=1
    else:i+=1
print("IMPOSSIBLE")
