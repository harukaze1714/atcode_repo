def func(n,d):
    return n//d

a,b,c=map(int,input().split())

if(a%c==0):
    print(func(b,c)-func(a,c)+1)
else:
    print(func(b,c)-func(a,c))