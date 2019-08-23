N,M = map(int, input().split())
mNum=0
MNum=10**10
for i in range(M):
    tm,tM = map(int, input().split())
    if(mNum<tm):
        mNum=tm
    if(MNum>tM):
        MNum=tM
print(max(MNum-mNum+1,0))