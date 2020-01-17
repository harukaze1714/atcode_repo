N,K = map(int,input().split())
R,S,P = map(int,input().split())
t=list(input())
q=['q']*K
t=t+q

s=0
for i in range(K,N+K):
    if t[-i-1] == t[-i-1+K]:
        t[-i-1]='q'
        continue
    elif t[-i-1] =='r':
        s+=P
    elif t[-i-1] =='s':
        s+=R
    elif t[-i-1] =='p':
        s+=S


print(s)