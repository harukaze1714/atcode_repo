C = input()
ans_n=0
h=""
f=1
for i in range(len(C)):
    if(f==2):
        ans_n+=1
        f=1
        h=C[i]
    elif(f==0):
        ans_n+=1
        f=2
        h=C[i]
    elif(h!=C[i]):
        ans_n+=1
        f=1
        h=C[i]
    else:
        f=0
        h=C[i]
print(ans_n)