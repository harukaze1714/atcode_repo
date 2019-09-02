import copy

N,B1,B2,B3=map(int, input().split())

A1=3
A2=7
A3=10
C=10

L=[0]*30
L2 = [[0] * N for i in range(N)]
R=[0]*30

ANS1 = [[0] * N for i in range(N)]
ANS2 = [[0] * N for i in range(N)]
ANS3 = [[0] * N for i in range(N)]

for i in range(N):
    L[i] = list(map(int, input().split()))

for i in range(N):
    R[i] = list(map(int, input().split()))

total1=0
total2=0
total3=0
for i in range(N-A3):
    for j in range(N-A3):
        for a in range(A3):
            ANS3[i][j]+=L[i][j+a]
        if(ANS3[i][j]==B1):
            total3+=1
#print(total3)

for c in range(C):
    for i in range(N-A3):
        for j in range(N-A3):
            for a in range(A3):
                if(B3-ANS3[i][j]==1):
                    if(L[i][j+a]<R[i][j+a]):
                        L[i][j+a]+=1
                    break
    total3=0
    for i in range(N-A3):
        for j in range(N-A3):
            ANS3[i][j]=0
            for a in range(A3):
                ANS3[i][j]+=L[i][j+a]
            if(ANS3[i][j]==B3):
                total3+=1
    #print("total3",total3)

for i in range(N):
    for j in range(N):
        L2[i][j]=L[i][j]

for i in range(N-A3):
    for j in range(N-A3):
        if(ANS3[i][j]==B1):
            for a in range(A3):
                L2[i][j+a]=99

#---------------------------------------------------------
total3=0
for i in range(N-A1):
    for j in range(N-A1):
        ANS1[i][j]=0
        for a in range(A1):
            ANS1[i][j]+=L2[i][j+a]
        if(ANS1[i][j]==B1):
            total3+=1
#print("total3",total3)
for c in range(C):
    for i in range(N-A1):
        for j in range(N-A1):
            for a in range(A1):
                if(B1-ANS1[i][j]==1):
                    if(L[i][j+a]<R[i][j+a]):
                        L[i][j+a]+=1
                        L2[i][j+a]+=1
                    break
    total3=0
    for i in range(N-A1):
        for j in range(N-A1):
            ANS1[i][j]=0
            for a in range(A1):
                ANS1[i][j]+=L2[i][j+a]
            if(ANS1[i][j]==B1):
                total3+=1
    #print("total3",total3)


#print("point")
for i in range(N):
    for j in range(N):
        print(L[i][j],end=" ")
    print()


