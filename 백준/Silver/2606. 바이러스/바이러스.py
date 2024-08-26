from collections import deque

def bfs(start):
    visited= [False] * (C+1)
    visited[start] = True
    queue = deque([start])
    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return sum(visited)



C = int(input())
graph = [[] for _ in range(C+1)]
E = int(input())
for _ in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(1)-1)