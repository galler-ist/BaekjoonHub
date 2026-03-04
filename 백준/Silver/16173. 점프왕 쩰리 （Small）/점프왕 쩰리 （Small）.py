dir = [(1,0),(0,1)]
def dfs():
    start =[(pan[0][0],0,0)]
    while start:
        move,y,x = start.pop()
        for d in dir:
            ny,nx = y+d[0]*move, x+d[1]*move
            if ny>=N or nx>=N:
                continue
            elif pan[ny][nx] == -1:
                print("HaruHaru")
                return
            else:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    start.append((pan[ny][nx],ny,nx))
    print("Hing")
    return
    
            
pan = []
N = int(input())
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    pan.append(list(map(int,input().split())))
dfs()
