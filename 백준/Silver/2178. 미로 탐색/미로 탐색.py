dir = [(1,0),(0,1),(-1,0),(0,-1)]

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
dp = [list(float("inf") for _ in range(M)) for _ in range(N)]
dp[0][0]=1

from collections import deque

dq = deque([(0,0)])
while dq:
    y,x = dq.popleft()
    if y==(N-1) and x==(M-1):
        break
    for dy, dx in dir:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=N or nx>=M:
            continue
        if arr[ny][nx]==0:
            continue
        if dp[ny][nx]>dp[y][x]+1:
            dp[ny][nx] = dp[y][x]+1
            dq.append([ny,nx])

print(dp[-1][-1])