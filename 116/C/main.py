N = int(input())
H = list(map(int, input().split()))

def calc(i,j):
    SUM=0
    T=H[i:j]
    TH=H
    if(len(T)==0):
        return 0
    
    tmp=min(T)
    for a in range(i,j):
        H[a]-=tmp
    SUM+=tmp
    
    List=[n for n, v in enumerate(T) if v == min(T)]

    if(len(T)>1):
        B=0
        for b in List:
            SUM+=calc(i+B,i+b)
            B=b+1
        SUM+=calc(i+B,j)

    return SUM


if __name__ == "__main__":

    print(calc(0,N))
    
    exit()


