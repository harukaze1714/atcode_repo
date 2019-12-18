import collections
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
A = list(map(int, input().split()))
List = {}
for i in A:
    if List.get(i,None)==None:
        List[i]=1
    else:
        List[i]+=1

List_sorted = sorted(List.items(), key=lambda x:x[1])
tmp=0
Num=len(List_sorted)-K

for i in range(Num):
    tmp+=list(List_sorted[0])[1]
    del List_sorted[0]

print(tmp)
