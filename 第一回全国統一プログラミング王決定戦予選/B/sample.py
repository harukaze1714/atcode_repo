def main():

    N = input()
    D = list(map(int,input().split()))
    M = max(D)
    countlist=[0] * (M + 1)
    ans=1

    for i in D:
        countlist[i]+=1

    if countlist[0]!=1 :
        ans = 0
    else :
        if D[0]!=0 :
            ans = 0
        else:
            for i in range(2,M+1):
                ans = (ans * (countlist[i-1]**countlist[i])) % 998244353

    print(ans) 

if __name__ == "__main__":
    main()
