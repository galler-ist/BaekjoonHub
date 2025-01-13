H, W = map(int,input().split())
blocks = list(map(int,input().split()))
max_H = max(blocks)
prefix = [0 for _ in range(W+2)]
suffix = [0 for _ in range(W+2)]
max_point = []

now_H= blocks[0]
for x in range(W+1):
    if blocks[x]==max_H:
        max_point.append(x)
        break
    now_H = max(blocks[x],now_H)
    prefix[x] = now_H+prefix[x-1]
    
now_H= blocks[-1]
for x in range(W-1,-1,-1):
    if blocks[x]==max_H:
        max_point.append(x)
        break
    now_H = max(blocks[x],now_H)
    suffix[x] = now_H+suffix[x+1]
result = max(prefix)+max(suffix) + (max_point[1]-max_point[0]+1)*max_H
print(result - sum(blocks))