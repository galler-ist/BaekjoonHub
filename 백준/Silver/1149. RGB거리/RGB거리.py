n = int(input())
r,g,b = map(int,input().split())
dp = [r,g,b]
for _ in range(n-1):
    r,g,b = map(int,input().split())
    temp1 = r + min(dp[1],dp[2])
    temp2 = g + min(dp[0],dp[2])
    temp3 = b + min(dp[0],dp[1])
    dp = [temp1,temp2,temp3]
print(min(dp))
