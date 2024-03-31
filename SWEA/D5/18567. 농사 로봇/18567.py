# 농사 로봇
import sys
import copy
sys.stdin = open('sample_input.txt','r')

directions1 = [(0,1),(-1,0),(0,-1),(1,0)]    # 위를 보고 있을 때
directions2 = [(1,0),(0,1),(-1,0),(0,-1)]    # 오른쪽을 보고 있을 때
directions3 = [(0,-1),(1,0),(0,1),(-1,0)]    # 아래를 보고 있을 때
directions4 = [(-1,0),(0,-1),(1,0),(0,1)]    # 왼쪽을 보고 있을 때

def robot(y,x,see):
    ssac = [[[0,100] for _ in range(N)] for _ in range(N)]
    this_arr = copy.deepcopy(arr)
    ssac_list = []
    # 만약 싹을 심으면 거기다가 +=1 해주고 필요한 time을 같이 적어주기
    time = 1
    result = 0
    my_dir = []

    afternoon = ""
    while time <=M:
        if see==(-1,0): my_dir = directions1
        elif see==(0,1): my_dir = directions2
        elif see==(1,0): my_dir = directions3
        elif see==(0,-1): my_dir = directions4
        # 오전
        if this_arr[y][x] == 4:
            result +=1
            this_arr[y][x]=0
            afternoon = "harvest"
        elif this_arr[y][x]==0:
            for dir in my_dir:
                ny,nx = y +dir[0], x + dir[1]
                if ny<0 or nx<0 or nx>=N or ny>=N : continue
                if this_arr[ny][nx]==0 or this_arr[ny][nx]==4:
                    ssac[y][x][0]+=1
                    ssac[y][x][1]= time+ssac[y][x][0]+4  # 이게 타임
                    this_arr[y][x]=2
                    ssac_list.append([y,x])
                    afternoon="ssac"
                    break
                
        # print(this_arr)
        # 오후
        if afternoon == "":
            pass
        elif afternoon == "ssac":
            # 오전에 새싹을 심은 경우
            y = ny
            x = nx
            see = dir
            afternoon = ""
        elif afternoon == "harvest":
            # 오전에 수확을 했으면 다음게 뭔지 아직 모름
            for dir in my_dir:
                ny, nx = y+dir[0], x + dir[1]
                if ny<0 or nx<0 or nx>=N or ny>=N : continue
                if this_arr[ny][nx]==0 or this_arr[ny][nx]==4:
                    y = ny
                    x = nx
                    see = dir
                    break
            afternoon = ""
        # 다음 날을 위한 준비
        if max_v >= (M-time) + result: return result
        time +=1
        # print(ssac_list,y,x, "지금의 싹과 로봇의 위치")
        # print(ssac)
        for j,i in ssac_list:
            if this_arr[j][i]==2 and time>=ssac[j][i][1]:
                this_arr[j][i]=4
                ssac_list.remove([j,i])
        
    # TODO: 나중 함수에서 (M-오늘의 날짜) + 수확 <=max_v : return하는 조건 만들기                    
    return result
            
    

def find_start():
    global max_v
    max_v=0
    for j in range(N):
        for i in range(N):
            if arr[j][i]==0:
                for see in [(0,1),(-1,0),(0,-1),(1,0)]:
                    temp_v = robot(j,i,see)
                    if temp_v>max_v:
                        max_v = temp_v
    return max_v


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())     # N: 한 변의 길이, M: 로봇이 동작하는 일의 수
    arr = [list(map(int,input().split())) for _ in range(N)] # 0:농지, 1:산
    # 0에다가 씨를 심으면 2를 넣고 시간이 1일 지나면 싹이 됨(3)
    # 지금의 싹이 그 자리에서 몇 번째인지 췌크!
    # ssak이라는 배열을 만들고, 싹을 심으면 거기에 +1을 해주고, 열리는 time을 총 농장 판에도 담아줌
    # 그리고 그 K 번째 + 3일 이후에 곡식(4)이 열림
    # TODO: 로봇의 할일 : (오전)
        # 1. 현재 농지가 0이며, 다음 0으로 이동할 수 있으면 2 심기
        # 2. 현재 농지가 0이며, 다음 0이 없는 경우 : 머무르기
        # 3. 현재 농지가 곡식(4)라면 그걸 0으로 만들고 result+=1
    # TODO: 로봇의 할 일 : (오후)
        # 1. 이동 가능한 곳은 0 or 4
        # 2. 이동 가능 한 곳이 여러 개면 이전 움직인 방향의 (*,*)에 따라서..
        # 3. 이동 가능 한 곳이 없으면 현재 위치에 머무르기
    # TODO: 이걸 M일 동안 반복!!!!
    print(f"#{tc} {find_start()}")
