import sys
input = sys.stdin.readline
n = int(input())

x_list = [0 for _ in range(1000000+1)]
y_list = [0 for _ in range(1000000+1)]
x_first,y_first = map(int,input().split())
x_before, y_before = x_first, y_first
min_x,min_y = x_first,y_first
max_x,max_y = x_first,y_first
for i in range(n-1):
    x,y = map(int,input().split())
    min_x,min_y = min(min_x,x) , min(min_y,y)
    max_x,max_y = max(max_x,x) , max(max_y,y)
    if x_before==x:
        y_list[min(y,y_before)]+=1
        y_list[max(y,y_before)]-=1
        y_before=y
    else:
        x_list[min(x,x_before)]+=1
        x_list[max(x,x_before)]-=1
        x_before=x
if x_before==x_first:
    y_list[min(y_first,y_before)]+=1
    y_list[max(y_first,y_before)]-=1
else:
    x_list[min(x_first,x_before)]+=1
    x_list[max(x_first,x_before)]-=1
        
# 이제 min_x부터 max_x까지 prefix
prefix_x = [0 for _ in range(min_x,max_x+1)]
for x in range(min_x,max_x):
    prefix_x[x-min_x+1] = prefix_x[x-min_x]+x_list[x]
    
prefix_y = [0 for _ in range(min_y,max_y+1)]
for y in range(min_y,max_y):
    prefix_y[y-min_y+1] = prefix_y[y-min_y]+y_list[y]


print(max(max(prefix_x),max(prefix_y)))

