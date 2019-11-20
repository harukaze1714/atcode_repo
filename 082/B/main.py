s=input()
l=input()

s=sorted(s)
l=list(reversed(sorted(l)))

#print(s,l)

if(s<l):
    print("Yes")
else:
    print("No")