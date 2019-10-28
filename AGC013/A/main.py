import collections
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

count=1
mode=0
for i,Num in enumerate(A):
    if(mode==0):
        mode=1
    elif(mode==1):
        if(A[i]==A[i-1]):
            mode=1
        elif(A[i]>A[i-1]):
            mode=2
        elif(A[i]<A[i-1]):
            mode=3
    elif(mode==2):
        if(A[i]<A[i-1]):
            mode=1
            count+=1
    elif(mode==3):
        if(A[i]>A[i-1]):
            mode=1
            count+=1

print(count)