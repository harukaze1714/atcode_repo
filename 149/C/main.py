
def cal(n):
    for i in range(2,int(n**0.5) + 1 ):
        if n%i == 0:
            return False
        
    return True


N=int(input())

i=0
while(True):
    if cal(N+i):
        print(N+i)
        exit()
    else:
        i+=1

