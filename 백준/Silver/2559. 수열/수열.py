import sys
input = sys.stdin.readline


N, K = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0 for _ in range(N)]

my_sum = 0
for idx,num in enumerate(arr):
    my_sum += num
    prefix[idx] = my_sum

result = prefix[K-1]
for i in range(K, N):
    temp = prefix[i]-prefix[i-K]
    result = max(temp,result)
print(result)