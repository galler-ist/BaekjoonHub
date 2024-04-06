import sys
sys.stdin = open("./sample_input.txt")
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def robot(y,x):
    for ty1,tx1,ty2,tx2,te in TUNNEL:
            if (tx1==x and ty1==y):
                if dp[ty2][tx2]<dp[y][x]+te: continue
                dp[ty2][tx2]= dp[y][x]+te
                # robot(ty2,tx2)
            if (tx2==x and ty2==y):
                if dp[ty1][tx1]<dp[y][x]+te: continue
                dp[ty1][tx1]= dp[y][x]+te
                # robot(ty1,tx1)
                                
    for dir in directions:
        ny, nx = y+dir[0], x+dir[1]
        if ny<=0 or nx<=0 or ny>N or nx>N:continue
        
        if MAP[ny][nx] < MAP[y][x]:
            move=0
        elif MAP[ny][nx] == MAP[y][x]:
            move=1
        else:
            move = 2*(MAP[ny][nx]-MAP[y][x])
        
        if dp[ny][nx]<dp[y][x]+move: continue
        dp[ny][nx] = dp[y][x]+move
        # robot(ny,nx)    
    return
            
        #TODO: tunnel 이 있으면 그 터널 해보고 그 위치에서 다시 robot 재귀
        #TODO: tunnel 해보고 이후 위치로 가서 또 재귀
        
    
T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())        # N:지도의 가로세로, M:터널 개수
    MAP = [[0 for _ in range(N+1)]] + [[0]+list(map(int,input().split())) for _ in range(N)]
    TUNNEL = [list(map(int,input().split())) for _ in range(M)] # Ay,Ax,By,Bx, 해당 터널을 쓸때의 연료량
    dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
    dp[1][1]=0
    # 1번만 하면 상하좌우로 움직이며 값이 변할 수 있음
    for _ in range(5):
        for j in range(1,N+1):
            for i in range(1,N+1):
                robot(j,i)
    # robot(1,1)
    print(f"#{tc} {dp[N][N]}")
    #TODO:만약 y,x가 터널의 입구라면 다음 함수에는 By,Bx를 넣고 연료는 그 터널의 값
    #TODO:방향은 무!조!건! 우측아래로는 아닌 듯
    
    