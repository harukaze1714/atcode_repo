A,B,C,D = map(int, input().split())

def gcd(c,d):
	if(c==0):
		return d
	else:
		return gcd(d%c,c)
prod = C*D
lcm = prod//gcd(C,D)

A-=1

AC=A//C
AD=A//D
BC=B//C
BD=B//D
ACD=A//lcm
BCD=B//lcm

print(B-A-BC-BD+BCD+AC+AD-ACD)
