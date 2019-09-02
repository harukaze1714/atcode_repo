S = int(input())
total=10*6
if(S%2==1):
    total=S*((S-1)//2)
else:
    total=(S-1)*((S-2)//2)+(S-1)

print(total)