

def calcA(S):
    Num=0
    for i in range (1,len(S)):
        A = int("".join(S[:i]))
        lenB=len(S[i:])
        Num += A*(2**(lenB-1))+calcA(S[i:])
    
    Num += int("".join(S))
    return Num


N = list(input())
print(calcA(N))
