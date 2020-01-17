N,A,B=map(int,input().split())

if(abs(A-B)%2==0):
    print(abs(A-B)//2)
else:
    o=max(abs(1-A),abs(1-B))
    n=max(abs(N-A),abs(N-B))
    t=min(o,n)

    t1=N-((A+B-1)//2)
    t2=((A+B+1)//2)-1
    print(min(t,t1,t2))

