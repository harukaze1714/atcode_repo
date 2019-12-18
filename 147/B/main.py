import math
s=list(input())
r=[0]*len(s)
for i in range(len(s)):
    r[len(s)-i-1]=s[i]

c=0
for i in range(len(s)//2):
    if(r[i]!=s[i]):
        c+=1

print(c)