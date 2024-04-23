directions =  [(0,1),(-1,0),(0,-1),(1,0)]
directions2 = [(0,1),(1,0),(0,-1),(-1,0)]

def cleaner(arr):
    next_arr = [[0 for _ in range(C)] for _ in range(R)]
    y = air_cleaner[0]
    # x 는 0임!
    # 하지만 시작 x는 1로 하는게 좋음
    # y,x를 기준으로 오른쪽, 위, 왼쪽, 아래
    #TODO: 여기서 x=0파트에서 무언가 이상함
    x=1
    next_arr[y][x]=0
    for dir in directions:
        while True:
            ny,nx = y+dir[0],x+dir[1]
            if ny<0 or nx<0 or ny>=R or nx>=C or arr[ny][nx]==-1:break
            next_arr[ny][nx]=arr[y][x]
            y,x = ny,nx
        
    # 밑에쪽은 시계방향
    y = air_cleaner[1]
    x = 1
    next_arr[y][x]=0
    for dir in directions2:
        while True:
            ny,nx = y+dir[0],x+dir[1]
            if ny<0 or nx<0 or ny>=R or nx>=C  or arr[ny][nx]==-1:break
            next_arr[ny][nx]=arr[y][x]
            y,x = ny,nx
    for y in range(R):
        for x in range(C):
            if y==0 or y==R-1 or x==0 or x==C-1 or y==air_cleaner[0] or y==air_cleaner[1]:continue
            next_arr[y][x] = arr[y][x]
    next_arr[air_cleaner[0]][0]=-1
    next_arr[air_cleaner[1]][0]=-1
    return next_arr
    

def misemunzi(arr):
    time = 0
    while time<T:
        time+=1
        temp_arr = [[0 for _ in range(C)] for _ in range(R)]
        for y in range(R):
            for x in range(C):
                if arr[y][x]<=0 : continue
                cnt = 0
                now = arr[y][x]
                diffusion = arr[y][x]//5
                for dir in directions:
                    ny, nx = y+dir[0], x+dir[1]
                    if ny<0 or nx<0 or ny>=R or nx>=C or arr[ny][nx]==-1 : continue
                    cnt +=1
                    temp_arr[ny][nx] += diffusion
                temp_arr[y][x] += (now-diffusion*cnt)
        temp_arr[air_cleaner[0]][0]=-1
        temp_arr[air_cleaner[1]][0]=-1
        next_arr = cleaner(temp_arr)
        arr = next_arr
    return arr
                    



R, C, T = map(int,input().split())  # R:행, C: 열 , T : time
air_cleaner = []
munzi = []
for y in range(R):
    temp = list(map(int,input().split()))
    munzi.append(temp)
    if len(air_cleaner)==2:continue
    for x in range(C):
        if temp[x]== -1:
            air_cleaner.append(y)
            break
result = 0
result_list=misemunzi(munzi)
for y in result_list:
    for x in y:
        if x==-1:continue
        result+=x
print(result)