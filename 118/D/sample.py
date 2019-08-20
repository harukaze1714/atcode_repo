# ABC 118 D
 
def resolve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
 
    costs = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
 
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(1, N+1):
        for a in A:
            if i - costs[a] < 0:
                continue
            dp[i] = max(dp[i-costs[a]] + 1, dp[i])
 
    ans = ""
    remain = dp[N]
    match = N
 
    minCosts = 10
    for a in A:
        minCosts = min(minCosts, costs[a])
 
    while match > 0:
        for a in A:
            if match - costs[a] < 0 or 1<= match - costs[a] < minCosts:
                continue
 
            if dp[match-costs[a]] == remain-1:
                ans += str(a)
                match -= costs[a]
                remain -= 1
                break
 
    print(ans)
 
 
if __name__ == "__main__":
    resolve()