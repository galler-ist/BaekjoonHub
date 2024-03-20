r = set()
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    r.update((j,i) for j in range(y1,y2) for i in range(x1,x2))
print(len(r))