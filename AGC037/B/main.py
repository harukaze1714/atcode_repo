MOD=998244353
import math
R=[]
B=[]
G=[]
A=""
sum=1
num=1
N=int(input())
C = input()
for i in range(N*3):
    if(C[i]=="R"):
        R.append(i)
    elif(C[i]=="G"):    
        G.append(i)
    else:
        B.append(i)
    if(A==C[i]):
       num+=1
    else:
        A=C[i]
        sum*=math.factorial(num)
        num=1

sum*=math.factorial(num)
sum*=math.factorial(N)

print(sum)