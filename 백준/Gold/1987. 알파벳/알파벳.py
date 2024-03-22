import sys

directions = [(1,0),(0,1),(-1,0),(0,-1)]

def alpha(y,x,now):
    global result, visited
    # if visited[ord(arr[y][x])-65]:
    #     result = max(result,now)
    #     return
    result = max(result, now)
    for dir in directions:
        ny, nx = y+dir[0], x+dir[1]
        if ny<0 or nx<0 or ny>=R or nx>=C: continue
        # if visited[ord(arr[ny][nx])-65] :       #TODO: 기저조건을 dir for문 안에 넣음
        #     result = max(result,now)
        #     continue
        if not visited[ord(arr[ny][nx])-65]:
            visited[ord(arr[ny][nx])-65]=True
            alpha(ny,nx,now+1)
            visited[ord(arr[ny][nx])-65]=False
            if result ==26:
                return
        
    return



R, C = map(int,sys.stdin.readline().split())
arr = [sys.stdin.readline() for _ in range(R)]
result=1
# visited=[[False]*C for _ in range(R)]
visited = [False]*26
visited[ord(arr[0][0])-65]=True
alpha(0,0,1)
print(result)
