def recur(idx, weight):
    global answer
    if weight > B:
        return -9999999
    
    if idx ==N:
        return 0
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    
    # 물건을 넣은 경우
    dp[idx][weight] = max(recur(idx+1, weight + items[idx][0])+items[idx][1],recur(idx+1, weight))
    
    return dp[idx][weight]

N, B = map(int,input().split())

items = [list(map(int,input().split())) for _ in range(N)]

dp = [[-1 for _ in range(100001)] for _ in range(N)]
result = recur(0,0)
print(result)