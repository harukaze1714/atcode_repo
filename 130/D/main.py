from sys import stdin

n,k = [int(x) for x in stdin.readline().rstrip().split()]
li = list(map(int,stdin.readline().rstrip().split()))

point = 0
r = 0
total = 0
for l in range(n):
    while r < n and total < k:
        total += li[r]
        r += 1
    #最後まで足してみたけどkに到達しなかったとき
    if total < k:
        break
    #rがかぶっている部分だけ1を足す
    else: 
        point += n-r+1
    #尺取り虫のように左を1進める(そしてその分トータルを減らす)
    total -= li[l]
print(point)
