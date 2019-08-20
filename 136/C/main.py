N = int(input())
H = list(map(int, input().split()))

cnt=0
cnt=H[0]
for i,num in enumerate(H):
    if(cnt>num):
        if(cnt>num+1):
            print("No")
            cnt=-1
            break
    else:
        cnt=num

if(cnt!=-1):
    print("Yes")
    