import heapq

N,M=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)

que = []
for a in A:
  heapq.heappush(que, -1*a)
 
for a in range(M):
  maxvalue = -1 * heapq.heappop(que)
  maxvalue /= 2
  heapq.heappush(que, -1*maxvalue)
 
print(sum([int(-1*a) for a in que]))
  