N, Q = map(int, input().split())
S = str(input())
J=[0]*N


for i in range(1,N):
    if((S[i-1]=="A")&(S[i]=="C")):
        J[i]=J[i-1]+1
    else:
        J[i]=J[i-1]


for i in range(Q):
    L, R = map(int, input().split())
    print(J[R-1]-J[L-1])
