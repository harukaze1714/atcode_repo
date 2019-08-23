N=[0]*9

N=21
for i in range(2**N):
    tmp2=""
    tmp=str(format(i, 'b'))
    for j in range(N-len(tmp)):
        tmp2+="0"
    tmp2+=tmp
    for i in range(N):
        if(int(tmp2[(N-1+i)%N])+int(tmp2[(N+1+i)%N]))%2!=int(tmp2[(N+i)%N]):
            break
    else:
        print(tmp2)
        print("OK")