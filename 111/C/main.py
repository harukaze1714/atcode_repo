N = int(input())
V = list(map(int, input().split()))

even = {}
odd = {}


for i in range(N):
    if(i%2==0):
        if odd.get(V[i],None)==None:
            odd[V[i]]=1
        else:
            odd[V[i]]+=1
    else:
        if even.get(V[i],None)==None:
            even[V[i]]=1
        else:
            even[V[i]]+=1


max_odd_k = max(odd, key=odd.get)
max_even_k = max(even, key=even.get)
max_odd_v = max(odd.values())
max_even_v = max(even.values())
len_odd = len(odd)
len_even = len(even)

if(max_odd_k!=max_even_k):
    print(N-max_odd_v-max_even_v)
    exit()

if((len_odd==1)&(len_even==1)):
    print(N//2)
    exit()


if(len_odd==1):
    del even[max_even_k]
    max2_even_v = max(even.values())
    print(N-max_odd_v-max2_even_v)
    exit()

if(len_even==1):
    del odd[max_odd_k]
    max2_odd_v = max(odd.values())
    print(N-max2_odd_v-max_even_v)
    exit()

del even[max_even_k]
max2_even_v = max(even.values())
del odd[max_odd_k]
max2_odd_v = max(odd.values())

print(min((N-max2_odd_v-max_even_v),(N-max_odd_v-max2_even_v)))
#print()
