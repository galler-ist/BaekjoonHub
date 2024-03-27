import sys
from heapq import heappop, heappush

def dijkstra(start):
    pq = []
    heappush(pq,(0,start))
    min_cows[start] = 0
    while pq :
        cow, loc = heappop(pq)
        if min_cows[loc]<cow:continue
        
        for next in graph[loc]:
            next_cow, next_loc = next
            new_cow = cow + next_cow
            if min_cows[next_loc]<=new_cow:continue
            min_cows[next_loc]=new_cow
            heappush(pq,(new_cow, next_loc))
            
    return
            
            
        
    

N, M = map(int,input().split()) #이후에 M줄에 A,B,C가 주어짐, 시작은 1, 목적지는 N
graph = [[] for _ in range(N+1)]
min_cows = [float('inf')] * (N+1)
start = 1
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))  # a<-->b 서로에게 c라는 소를 넣음
dijkstra(start)
print(min_cows[N])
