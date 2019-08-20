import heapq
N,M = [int(i) for i in input().split()]
AB = [[int(i) for i in input().split()] for j in range(N)]
AB.sort(key=lambda x:x[0])
index = 0
Works = []
ans = 0

for d in range(1,M+1):#d日後までの支払いのうち一番高いやつ
    while 1:
        if index>=N:break
        if AB[index][0]<=d:
            heapq.heappush(Works,-AB[index][1])
            index += 1
        else:
            break
    if Works:
        ans -= heapq.heappop(Works)
print(ans)
