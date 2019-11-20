import math
MOD=10**9+7
X , Y =map(int,input().split())
X1=X
Y1=Y
x=0
y=0
if(X>Y):
    x=X-Y
    X1-=2*x
    Y1-=x
else:
    y=Y-X
    X1-=y
    Y1-=2*y
if(X1<0 or Y1<0 or X1%3!=0 or Y1%3!=0):
    print(0)
    exit()
x+=X1//3
y+=X1//3


List1=[1]*(x+y+1)
List2=[1]*(x+y+1)
List3=[1]*(x+y+1)

for i in range(1,x+y+1):
    List1[i]=(List1[i-1]*i)%MOD
    List2[i]=MOD - List2[MOD % i] * (MOD // i) % MOD
    List3[i] =   List3[i - 1] * List2[i] % MOD

print(List1[x+y] * (List3[y] * List3[x] % MOD) % MOD)







x, y = map(int, input().split())

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
  
mod = 10**9+7 #出力の制限
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1]

if (x+y)%3 != 0 :
  print(0)
else:
  n = (x + y) // 3
  if x >= n and y >= n:
    a = x - n
    b = y - n
    
    for i in range(2, n + 1):
      g1.append( ( g1[-1] * i ) % mod )
      inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
      g2.append( (g2[-1] * inverse[-1]) % mod )
    
    answer = cmb(a+b,a,mod)
    print(answer)
  else:
    print(0)
