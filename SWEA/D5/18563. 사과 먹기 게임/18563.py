from collections import deque
# 사과 먹기 게임
import sys
sys.stdin = open('sample_input.txt','r')
def find_M(num):
    M=1
    while M*(M+1)//2<num:
        M+=1
    return M
    # for M in range(1,num):
    #     if num==(M*(M+1)//2):
            # return M
def eat_apple(q):
    result = 0
    now_dir = "right"
    y, x = q.popleft()
    while q:
        gy, gx = q.popleft()
        # now_dir가 어디인지
        if y<gy :   #밑에
            if x<gx : # 오른쪽에
                if now_dir=="up":      #TODO : 내가 위를 보고있으면 +2
                    result+=2  
                    now_dir="down"
                elif now_dir=="right": #TODO : 내가 오른쪽을 보고 있으면 +1
                    result +=1
                    now_dir="down"
                elif now_dir =="left": #TODO : 내가 왼쪽을 보고 있으면 +3
                    result +=3
                    now_dir="down"
                elif now_dir =="down": #TODO : 내가 밑을 보고 있으면 +3
                    result +=3
                    now_dir = "right"

            else: #왼쪽에
                if now_dir=="up":
                    result+=3
                    now_dir="left"
                elif now_dir=="right":
                    result+=2
                    now_dir="left"
                elif now_dir=="left":
                    result+=3
                    now_dir="down"
                elif now_dir=="down":
                    result+=1
                    now_dir="left"
                #TODO: 내가 위를 보고 있으면 +3
                #TODO: 내가 오른쪽을 보고 있으면 +2
                #TODO: 내가 왼쪽을 보고 있으면 +3
                #TODO: 내가 밑을 보고 있으면 +1
        else:       # 위에
            if x<gx : # 오른쪽에
                if now_dir=="up":
                    result+=1
                    now_dir="right"
                elif now_dir=="right":
                    result+=3
                    now_dir="up"
                elif now_dir=="left":
                    result+=2
                    now_dir="right"
                elif now_dir=="down":
                    result+=3
                    now_dir="right"
                #TODO : 내가 위를 보고있으면 +1
                #TODO : 내가 오른쪽을 보고 있으면 +3 
                #TODO : 내가 왼쪽을 보고 있으면 +2
                #TODO : 내가 밑을 보고 있으면 +3
            else :  #왼쪽에
                if now_dir=="up":
                    result+=3
                    now_dir="left"
                elif now_dir=="right":
                    result+=3
                    now_dir="up"
                elif now_dir=="left":
                    result+=1
                    now_dir="up"
                elif now_dir=="down":
                    result+=2
                    now_dir="up"
                #TODO : 내가 위를 보고있으면 +3
                #TODO : 내가 오른쪽을 보고 있으면 +3
                #TODO : 내가 왼쪽을 보고 있으면 +1
                #TODO : 내가 밑을 보고 있으면 +2
        y , x = gy,gx
    return result
    
# 현재 나의 방향 * 나의 위치를 기준으로 다음 숫자의 사분면


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # arr에는 총 몇 번까지 있는지 sum으로 보겠다
    arr_sum=0
    for j in arr: arr_sum +=sum(j)
    M = find_M(arr_sum)
    M_list = deque([0,0] for _ in range(M+1))
    for j in range(1,N-1):
        for i in range(1,N-1):
            num = arr[j][i]
            if 0<num<=M:
                M_list[num]=[j,i]
    # tc 1 [[0, 0], [2, 1], [3, 2], [1, 3]]
    print(f"#{tc} {eat_apple(M_list)}")
    