s=list(input())

for i in range(len(s)):
    if(s[i]=="B"):
        s[i]="A"
        for j in range(i,-1,-1):
            if((s[j]=="0")|(s[j]=="1")):
                s[j]="A"
                break

for C in s:
    if(C!="A"):
        print(C,end="")

