
N = int(input())
s = list(input())
t = list(input())

tmp=0
for i in range(N):
    for j in range(N):
        if(s[j]==t[i]):
            for k in range(N-1,j,-1):
                tmp=0
                if(s[k]!=t[k-j]):
                    tmp=1
                    break
            if(tmp==0):
                print(N+j)
                exit()
print(N*2)
