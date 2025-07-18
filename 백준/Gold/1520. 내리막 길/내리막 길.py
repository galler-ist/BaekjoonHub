import sys
sys.setrecursionlimit(300000)

dir = [0,1],[0,-1],[1,0],[-1,0]


def recur(y,x):
    
    
    
    if y == Y-1 and x == X-1:
        return 1
    
    if dp[y][x] != -1 :
        return dp[y][x]
    route = 0

    for dy, dx in dir:
        ey, ex = y + dy, x + dx
        
        if 0<=ey <Y and 0<=ex<X :
            if graph[y][x] > graph[ey][ex]:
                route += recur(ey,ex)
    dp[y][x] = route
    return route

Y, X = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(Y)]
dp = [[-1 for _ in range(X)] for _ in range(Y)]


answer = recur(0,0)
print(answer)
# print(dp)