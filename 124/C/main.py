O = input()
N = len(O)
total0=0
total1=0

for i in range(N):
    if(int(O[i])==i%2):
        total0+=1
    else:
        total1+=1

print(min(total0,total1))