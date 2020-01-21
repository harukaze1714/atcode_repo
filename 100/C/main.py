N = int(input())
A = list(map(int, input().split()))

t=0
c=0
while(N>c):
    if(A[c]%2==0):
        t+=1
        A[c]//=2
    else:
        c+=1
print(t)