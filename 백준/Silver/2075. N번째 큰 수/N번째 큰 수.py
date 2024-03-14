import sys
import heapq
N = int(input())
myheap=[]
j=0
for _ in range(N):
    numbers=list(map(int,sys.stdin.readline().split()))
    for num in numbers:
        if len(myheap)<N:
            heapq.heappush(myheap, num)
        else:
            my_min=heapq.heappop(myheap)
            heapq.heappush(myheap,max(my_min,num))
print(heapq.heappop(myheap))