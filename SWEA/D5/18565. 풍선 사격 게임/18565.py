# 18565. 풍선 사격 게임
import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def ballon(arr):
    global result
    q = deque()
    q.append((arr,0))
    while q:
        *temp,score = q.popleft()
        if len(temp[0])==3:
            a,b,c = temp[0]
            #TODO: 처음에 a를 터트린다면 b + 2b/2c
            #TODO: 처음에 c를 터트린다면 b + 2b/2a
            #TODO: 처음에 b를 터트린다면 ac+a+c
            result = max(result,score+max(3*b,b+2*c,b+2*a,a*c+2*a,a*c+2*c))
            continue
        for idx, num in enumerate(temp[0]):
            if len(temp[0])==1:
                result = max(result,score+num)
            elif idx==0:
                new_arr = temp[0][1:]
                q.append((new_arr,score+temp[0][idx+1]))
            elif  idx==len(temp[0])-1:
                new_arr = temp[0][:idx]
                q.append((new_arr,score+temp[0][idx-1]))
            elif 0<idx<len(temp[0])-1:
                new_arr = temp[0][:idx] + temp[0][idx+1:]
                q.append((new_arr,score+(temp[0][idx-1]*temp[0][idx+1])))
    return
            
    #TODO: while q 에다가 ([남은 풍선리스트], 점수) 를 q에 계속 넣음




T = int(input())
for tc in range(1,T+1):
    N = int(input())    # N:풍선 개수
    Ballons = list(map(int,input().split()))    # 여기에 풍선 리스트
    result = 0
    ballon(Ballons)
    print(f"#{tc} {result}")
    # TODO: 풍선이 터지면 풍선이 이동됨
    # 풍선 점수
    # TODO: 풍선이 터지면 좌우로 이웃한 두 숫자의 곱
    # TODO: 1개만 있으면 그 숫자가 점수
    # TODO: 혼자만 있다면(이웃하는게 없으면) 그 풍선의 숫자를 점수로 얻음