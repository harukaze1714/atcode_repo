"""
for N in range(1000):
    #N=int(input())

    for i in range(10**10):
        t=format(i,"b")
        s=0
        for j in range(len(t)):
            s+=int(t[-j-1])*(-2)**(j)
        
        if(s==N):
            break
        s=0
    print(s,t)
"""
for i in range(10**3):
    t=format(i,"b")
    s=0
    for j in range(len(t)):
        s+=int(t[-j-1])*(-2)**(j)
    print(i,s,t)