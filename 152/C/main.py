N = int(input())
A = list(map(int, input().split()))
t=10**10
c=0
for a in A:
    if(a<=t):
        c+=1
        t=a
print(c)