from collections import deque
dirs = [(-1,0),(0,-1),(0,1),(1,0)]

def iceberg(pan):
    global time
    time = 0
    while True:
        pan_next = list(list(0 for _ in range(M)) for _ in range(N))
        first = []
        for y in range(1,N-1):
            for x in range(1,M-1):
                if pan[y][x]==0:
                    continue
                fuze = 0
                for dy,dx in dirs:
                    if pan[y+dy][x+dx]==0:
                        fuze +=1
                pan_next[y][x] = max(pan[y][x]-fuze,0)
                if (pan_next[y][x]!=0) & (first==[]):
                    first.append([y,x])
        pan = pan_next
        time +=1     
        # 빙산이 몇 개의 구역으로 되어있는지 체크
        if first:
            # 체크해보면 됨
            if check_fuzes(pan_next,first):
                return time
        else:
            time = 0
            return time
        
        
            
def check_fuzes(check_pan,first):
    start = first[0]
    # ices는 숫자의 총합
    now_ices = sum(sum(row) for row in check_pan)
    first_ices = 0
    ice_list = deque()
    ice_list.append(start)
    
    # 방문 여부를 기록하는 visited 배열
    visited = [[False] * len(check_pan[0]) for _ in range(len(check_pan))]
    visited[start[0]][start[1]] = True
    
    while ice_list:
        y,x = ice_list.popleft()
        first_ices += check_pan[y][x]
        for dy,dx in dirs:
            ny, nx = y+dy, x+dx
            if not visited[ny][nx] and check_pan[ny][nx] > 0:
                ice_list.append((ny,nx))
                visited[ny][nx] = True
    return now_ices != first_ices
    
                
                
    


N, M = map(int,input().split())
waters = []
for _ in range(N):
    waters.append(list(map(int,input().split())))
    

result = iceberg(waters)
    
print(result)