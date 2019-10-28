N, A, B = map(int, input().split())

if(B-A<0):
    print("0")
    exit()
if(A==B):
    if(N==1):
        print("1")
        exit()
    else:
        print("0")
        exit()
if(N==1):
    if(A==B):
        print("1")
        exit()
    else:
        print("0")
        exit()

if(N==2):
    print("1")
    exit()

print(B*(N-2)-A*(N-2)+1)



