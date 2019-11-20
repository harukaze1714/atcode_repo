N=int(input())


for i in range(1,N+1):
    S=""
    if(i%2==0):S+="a"
    if(i%3==0):S+="b"
    if(i%4==0):S+="c"
    if(i%5==0):S+="d"
    if(i%6==0):S+="e"
    if(S==""):S=i
    print(S)