N, T = map(int,input().split())
tests = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(T+1) for _ in range(N+1)]

for i in range(1,N+1):
    k,s = tests[i-1]
    for j in range(1, T+1):
        if j<k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k]+s)
            
print(dp[-1][-1])