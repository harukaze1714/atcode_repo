x,y = map(int,input().split())

if(x>=0 and y>0):
    if(abs(x)>abs(y)):
        print(abs(x-y)+2)
    else:
        print(abs(x-y))

if(x>=0 and y<=0):
    if(abs(x)>abs(y)):
        print(abs(x+y)+1)
    else:
        print(abs(x+y)+1)
        
if(x<0 and y>0):
    if(abs(x)>abs(y)):
        print(abs(x+y)+1)
    else:
        print(abs(x+y)+1)
        
if(x<0 and y<=0):
    if(abs(x)>abs(y)):
        print(abs(x-y))
    else:
        print(abs(x-y)+2)
        