A ,B = map(int, input().split())

NUM=1
for i in range(1000):
    if(NUM>=B):
        break
    
    NUM=NUM-1+A

print(i)