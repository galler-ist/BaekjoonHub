import sys
import heapq
from collections import deque
N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
rheap=list((arr[j][0] for j in range(N)))
def bigger(i):
    global rheap,arr
    for j in range(N-1,-1,-1):
        want = heapq.heappop(rheap)
        if want>arr[j][i]:
            heapq.heappush(rheap,want)
            return
        heapq.heappush(rheap,arr[j][i])
    return
    


for i in range(1,N):
    bigger(i)
print(heapq.heappop(rheap))