sum_square=0
arr = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(y1,y2):
        for i in range(x1,x2):
            arr[j][i]+=1

for j in range(100):
    for i in range(100):
        if arr[j][i]!=0: sum_square+=1
print(sum_square)