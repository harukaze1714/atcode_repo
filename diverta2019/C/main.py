N=int(input())
s=0
BA=0
XA=0
BX=0
for i in range(N):
    st=input()
    s+=st.count("AB")
    f1=0
    f2=0

    
    if(st[0]=="B"):f1=1
    if(st[-1]=="A"):f2=1

    if(f1 and f2):
        BA+=1
    elif(f1):
        BX+=1
    elif(f2):
        XA+=1
if(XA==0 and BX==0 and BA<2):
    print(s)
elif(XA==0 and BX==0):
    print(s+BA-1)
else:
    print(s+min(XA+BA,BX+BA))