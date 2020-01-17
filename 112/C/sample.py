import random

X=random.randint(0,100)
Y=random.randint(0,100)
H=400
print(X,Y,H)
N=10
print(N)
for i in range(N):
    x=random.randint(0,100)
    y=random.randint(0,100)
    print(x,y,H-abs(X-x)-abs(Y-y))
