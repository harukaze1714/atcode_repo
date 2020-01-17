s=input()
N=int(input())
#s="atcoderandatcodeera"
#N=5
D={}

if(len(s)<=1):
    for i in range(1,len(s)+1):
        for j in range(len(s)):
            if D.get(s[j:j+i],None) == None:
                D[s[j:j+i]]=1
    D=sorted(D)
    print(D[N-1])
    exit()
else:
    t=sorted(s)
    i=0
    k=0
    for c in t:
        if(c!=k):
            i=0
            if(len(D)>=5):
                break
        k=c
        while(i<len(s)):
            if(s[i]==c):
                break
            i+=1
        j=i+1
        while(j<=min(len(s),i+5)):
            D[s[i:j]]=1
            j+=1
        i+=1
    
    D=sorted(D)
    print(D[N-1])
    exit()



