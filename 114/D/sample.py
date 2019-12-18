N=999999999
n=list(str(N))[0]
n=int(("").join(n))
l=len(str(N))
if(l<7):
    c=0
    for i in range(N):
        s=str(i)
        if(s.find("7")>=0 and s.find("5")>=0 and s.find("3")>=0 ):
            c+=1
    print(c)
else:
    c=0
    for i in range(10**7):
        st=str(i)
        if(st.find("7")>=0 and st.find("5")>=0 and st.find("3")>=0 ):
            c+=1

    if(n>=7):t=3
    elif(n>=5):t=2
    else:t=1

    for i in range(6,l-1):
        c+=(3**(i))-(6*(i-1))-3
    c+=(3**(l-1))*t
    print(c)

