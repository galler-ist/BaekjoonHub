from heapq import heappop
N = int(input())
arr = sorted([int(input()) for _ in range(N)])
result=0
while len(arr)>=2:
    a=heappop(arr)
    b=heappop(arr)
    result+=(a+b)
    arr.append(a+b)
print(result)