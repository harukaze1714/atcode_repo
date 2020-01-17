N=input()
if(N[1:len(N)].count("9")!=len(N)-1):
    print(int(N[0])-1+9*(len(N)-1))
else:
    print(int(N[0])+9*(len(N)-1))

