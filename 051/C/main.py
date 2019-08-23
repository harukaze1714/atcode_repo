H = list(map(int, input().split()))
SX=H[0]
SY=H[1]
TX=H[2]
TY=H[3]
TX=TX-SX
TY=TY-SY

if((TX>=0)&(TY>=0)):
    U="U"
    R="R"
    D="D"
    L="L"

if((TX<0)&(TY>=0)):
    U="U"
    R="L"
    D="D"
    L="R"

if((TX>=0)&(TY<0)):
    U="D"
    R="R"
    D="U"
    L="L"

if((TX<0)&(TY<0)):
    U="D"
    R="L"
    D="U"
    L="R"

for i in range(abs(TY)):print(U,end="") 
for i in range(abs(TX)):print(R,end="") 

for i in range(abs(TY)):print(D,end="")
for i in range(abs(TX)):print(L,end="") 

print(L,end="") 
for i in range(abs(TY)+1):print(U,end="")
for i in range(abs(TX)+1):print(R,end="") 
print(D,end="")

print(R,end="") 
for i in range(abs(TY)+1):print(D,end="")
for i in range(abs(TX)+1):print(L,end="") 
print(U,end="")

