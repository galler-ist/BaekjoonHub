N, K = map(int,input().split())
bag = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)] # 행: 가방 개수, 열: 무게 오름차순

for i in range(1,N+1):
    w,v = bag[i-1]
    for j in range(1, K+1):
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[-1][-1])
