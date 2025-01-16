import sys
input = sys.stdin.readline
def prefix(pans):
    result_pan = [list(0 for _ in range(N+1)) for _ in range(N+1)]
    for y in range(1,N+1):
        for x in range(1,N+1):
            result_pan[y][x] = result_pan[y-1][x]+result_pan[y][x-1]-result_pan[y-1][x-1]+pans[y-1][x-1]
    return result_pan

N,M = map(int,input().split())
pans = []
for _ in range(N):
    pan = list(map(int,input().split()))
    pans.append(pan)
prefix_pan = prefix(pans)
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = prefix_pan[x2][y2]-prefix_pan[x2][y1-1]-prefix_pan[x1-1][y2]+prefix_pan[x1-1][y1-1]
    print(result)