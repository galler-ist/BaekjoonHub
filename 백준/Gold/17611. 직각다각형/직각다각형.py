N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

MID = 500_000
TOTAL = MID * 2 + 1
H, V = 0, 1

def solve(hv):
    line = [0] * TOTAL
    for cur in range(hv, N, 2):
        nxt = (cur + 1) if cur + 1 != N else 0
        j = 0
        if arr[cur][0] == arr[nxt][0]:
            j = 1
        min_p, max_p = sorted([arr[cur][j], arr[nxt][j]])
        line[min_p + MID] += 1
        line[max_p + MID] -= 1
    
    ans, tot = 0, 0    
    for i in line:
        tot += i
        ans = max(ans, tot)
    return ans

ans = max(solve(H), solve(V))
print(ans)