#N=3485
#A=[ 32, 1, 87, 25, 36]
N=int(input())


for i in range(1,3501):
    for j in range(1,3501):
        u=-N*i*j
        d=N*i+N*j-4*i*j
        if(d!=0):
            if(u%d==0 and (u*d > 0)):
                k=u//d
                if(N*(i*j+j*k+k*i)==4*i*j*k):
                    print(i,j,k)
                    exit()