
def storage(buildings):
    # 첫 점과 마지막 위치 알아내서 그 안에서만 할거다.
    # 중간 점은 high_L
    # start = buildings[0][0]
    # end = buildings[-1][0]
    now = 0
    now_L = buildings[now][0]
    now_H = buildings[now][1]
    result = 0
    while now_L<high_L:
        now_H = max(now_H, buildings[now][1])
        result += (now_H * (buildings[now+1][0]-buildings[now][0]))
        now+=1
        now_L = buildings[now][0]
    final_L = now_L
    now = N-1
    now_L = buildings[now][0]
    now_H = buildings[now][1]
    while now_L>final_L:
        now_H = max(now_H, buildings[now][1])
        result += (now_H * (buildings[now][0]-buildings[now-1][0]))
        now-=1
        now_L = buildings[now][0]
    final2_L = now_L
    if final_L<=final2_L:
        result += (final2_L-final_L+1) * high_H
    return result





# 가장 높은 값을 기준으로 왼쪽, 오른쪽으로 나눈다.
N = int(input())
buildings = []
high_H = 0
high_L = 0
for _ in range(N):
    L,H = map(int,input().split())
    if H>high_H:
        high_H = H
        high_L = L
    buildings.append((L,H))
# 위치 L에 따라서 정렬
buildings.sort(key=lambda x: x[0])
answer = storage(buildings)
print(answer)