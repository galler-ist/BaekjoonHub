
N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int,input().split())))
result = 0
dp = [0 for _ in range(N)]
dp[0] = meetings[0][2]
for i in range(1,N):
    # 이번 회의를 참가했을 때 
    dp[i] = max(dp[i-1], dp[i-2] + meetings[i][2])

print(dp[-1])