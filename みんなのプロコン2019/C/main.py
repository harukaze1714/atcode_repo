K,A,B = map(int, input().split())

S=K+1
diff=B-A
t=((K-A+1)//2)
T=diff*t
odd=((K-A+1)%2)
print(max(T+odd+A,S))