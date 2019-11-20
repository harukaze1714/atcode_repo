def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

x, y = map(int, input().split())

mod = 10**9+7 #出力の制限
g1 = [1]*(x+y) # 元テーブル
g2 = [1]*(x+y) #逆元テーブル
inverse = [1]*(x+y)
inverse[0] = 1

if (x+y)%3 != 0 :
  print(0)
else:
  n = (x + y) // 3
  if x >= n and y >= n:
    a = x - n
    b = y - n
    
    for i in range(2, n + 1):
      g1[i]=( g1[i-1] * i ) % mod 
      inverse[i]=( -inverse[mod % i] * (mod//i) ) % mod 
      g2[i]=(g2[i-1] * inverse[i]) % mod
    
    answer = cmb(a+b,a,mod)
    print(answer)
  else:
    print(0)
