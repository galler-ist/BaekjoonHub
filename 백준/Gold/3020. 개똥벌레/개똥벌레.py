# 장애물은 아래, 위, 아래, 위 순서대로 생긴다.
# N은 동굴의 길이(장애물 개수), H는 높이!
import sys
input = sys.stdin.readline

N, H = map(int,input().split())
# hurdles=[[0 for _ in range(H+1)] for _ in range(N)]
hurdles = [0 for _ in range(H+1)]
for i in range(N):
    # i가 짝수라면 밑에서, 홀수라면 위에서
    height = int(input())
    if i%2==0:
        hurdles[0]+=1
        hurdles[height]-=1
    else:
        hurdles[H-height]+=1
prefix = [0 for _ in range(H+1)]
for i in range(H):
    prefix[i+1] = hurdles[i] + prefix[i]
min, cnt = float('inf'),0

for idx in range(1,H+1):
    if min>prefix[idx]:
        cnt = 1
        min = prefix[idx]
    elif min==prefix[idx]:
        cnt +=1
print(min, cnt)