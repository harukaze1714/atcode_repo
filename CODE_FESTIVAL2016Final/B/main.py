N=int(input())

for i in range(1,N+1):
    if(N<=(i*(i+1)//2)):
        print(i)
        if(N==1 or N==2):
            exit()
        M=N-i
        j=i-1
        while(M>0):
            if(M>=j):
                M-=j
                print(j)
            j-=1
        exit()
            
        

