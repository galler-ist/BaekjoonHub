def recur(idx, A, B, C, D, E, my_list):
    global answer, answer_list
    # 중간이라도 모든 필요영양소를 충족했다면
    if a<=A and b<=B and c<=C and d<=D:
        if answer>E:            
            answer = E
            answer_list = my_list
        return
    if idx==N:
        return
    
    temp_list = []
    for i in my_list:
        temp_list.append(i)
    temp_list.append(idx+1)
    if answer<E:
        return
    # 재료를 사용하면 영양소 더해짐
    recur(idx+1, A+ingre[idx][0], B+ingre[idx][1], C+ingre[idx][2], D+ingre[idx][3], E+ingre[idx][4], temp_list)
    # 재료를 사용 안 하면 다음 재료로 넘어감
    recur(idx+1, A, B, C, D, E, my_list)
    
N = int(input())
a, b, c, d = map(int,input().split())
ingre = [list(map(int,input().split())) for _ in range(N)]
answer = float('inf')
answer_list = []
recur(0, 0, 0, 0, 0, 0, [])
if answer == float('inf'):
    print(-1)
else:
    print(answer)
    print(*answer_list)