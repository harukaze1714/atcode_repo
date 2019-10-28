C = []
for i in range(3):
    C.append([int(c) for c in input().split()])

ans = "Yes"
tmp=C[0][0]

A=[0]*3
B=[0]*3
for i in range(3):
    B[i]=C[0][i]
for i in range(3):
    A[i]=C[i][0]-B[0]

for i in range(3):
    for j in range(3):
        if(C[i][j]!=A[i]+B[j]):
            ans = "No"
            
print(ans)
