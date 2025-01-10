dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
def shark(balls):
    pan = [list(([] for _ in range(N))) for _ in range(N)]
    ball_list = [] # 위치정보 담김
    for ball in balls:
        pan[ball[0]-1][ball[1]-1] = [ball[2:5]] # m,s,d 순서서
        ball_list.append([ball[0]-1, ball[1]-1])
        
    for _ in range(K):
        pan_temp = [list(([] for _ in range(N))) for _ in range(N)]
        ball_list_temp = []
        engraft_list = set()
        for ball in ball_list:
            r,c = ball
            for length in range(len(pan[r][c])):
                m,s,d = pan[r][c][length]
                r_n = (r+dir[d][0]*s)%N
                c_n = (c+dir[d][1]*s)%N
                pan_temp[r_n][c_n].append([m,s,d])
                if (r_n,c_n) in ball_list_temp:
                    engraft_list.add((r_n,c_n))
                else:
                    ball_list_temp.append((r_n,c_n))
                
        for engraft in engraft_list:
            r,c = engraft # 터질 장소
            m,s,d=0,0,0
            ball_N = len(pan_temp[r][c])
            ds=[]
            # zerodivision 방지
            if ball_N>0:
                for engraft_ball in pan_temp[r][c]:
                    m += engraft_ball[0]
                    s += engraft_ball[1]
                    ds.append(engraft_ball[2])
                m_n = m//5
                s_n = s//ball_N
                d_n = check_oddeven(ds)
                if m_n>0:
                    pan_temp[r][c] = [[m_n,s_n,d_nn] for d_nn in d_n]
                else:
                    pan_temp[r][c] = []
                    ball_list_temp.remove((r,c)) # 만약 소멸되면 ball_list에서도 지워주기기
                    # 질량이 작으면 소멸
            else:
                continue

            
        ball_list = ball_list_temp
        pan = pan_temp
    
    Ms = 0
    for ball in ball_list:
        r,c = ball
        for ball_info in pan[r][c]:
            Ms+=ball_info[0]

    
    return Ms

def check_oddeven(d_list):
    if d_list[0]%2:
        odd_even = "odd"
    else:
        odd_even = "even"
    
    for check in d_list[1:]:
        if ((odd_even=="odd") & (check%2==1)) or ((odd_even=="even") & (check%2==0)):
            continue
        else:
            return [1,3,5,7]
    return [0,2,4,6]
    

N, M, K = map(int,input().split())
balls = []
for _ in range(M):
    balls.append(list(map(int,input().split()))) # r,c,m,s,d
result = shark(balls)
print(result)