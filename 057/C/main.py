def number(a):
    m=10**10
    MAX=int(a**0.5)+1
    for i in range(1,MAX):
        if(a%i==0):
            b=len(str(i))
            c=len(str(a//i))
            m=min(m,max(b,c))
    return m

N=int(input())
print(number(N))