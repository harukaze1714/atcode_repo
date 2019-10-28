import math

A,B,X = map(int, input().split())

x=X/(A*A)
x2=X/A

if(x2>=((A*B)/2)):
    #b2=B-(2*x2-A*B)/A
    #print(90*(b2/A))
    tmp=(2*A*A*B-2*X)
    tmp2=A*A*A
    print(round(math.degrees(math.atan(tmp/tmp2)),10))
else:
    tmp=(A*B*B)
    tmp2=2*X
    print(round(math.degrees(math.atan(tmp/tmp2)),10))
#    print(90*(B/a2))
#    print(math.degrees(math.tan(B/a2)))