N,B1,B2,B3=map(int, input().split())

A1=3
A2=7
A3=7
C=10

L=[0]*30
L2 = [[0] * N for i in range(N)]
R=[0]*30

#ANS1 = [[0] * N for i in range(N)]
#ANS2 = [[0] * N for i in range(N)]
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
                    if((L[i][j+a]+1<R[i][j+a])&(L2[i][j+a]==0)):
                        L[i][j+a]+=1
                    break
            for a in range(A3):
                if(B3-ANS3[i][j]==2):
                    if((L[i][j+a]+2<R[i][j+a])&(L2[i][j+a]==0)):
                        L[i][j+a]+=2
                    break
    total3=0
    for i in range(N-A3):
        for j in range(N-A3):
            ANS3[i][j]=0
            for a in range(A3):
                ANS3[i][j]+=L[i][j+a]
            if(ANS3[i][j]==B3):
                total3+=1
                for a in range(A3):
                    L2[i][j+a]=1
    #print("total3",total3)

    for i in range(N-A3):
        for j in range(N-A3):
            for a in range(A3):
                if(B3-ANS3[i][j]==1):
                    if((L[i+a][j]+1<R[i+a][j])&(L2[i+a][j]==0)):
                        L[i+a][j]+=1
                    break
            for a in range(A3):
                if(B3-ANS3[i][j]==2):
                    if((L[i+a][j]+2<R[i+a][j])&(L2[i+a][j]==0)):
                        L[i+a][j]+=2
                    break
    total2=0
    for i in range(N-A3):
        for j in range(N-A3):
            ANS3[i][j]=0
            for a in range(A3):
                ANS3[i][j]+=L[i+a][j]
            if(ANS3[i][j]==B3):
                total2+=1
                for a in range(A3):
                    L2[i+a][j]=1
    #print("total2",total2)


#print("point")
for i in range(N):
    for j in range(N):
        print(L[i][j],end=" ")
    print()


