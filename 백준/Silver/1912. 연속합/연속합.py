N = int(input())
num_list = list(map(int,input().split()))
prefix = [0 for _ in range(N+1)]
# prefix[0] = num_list[0]
for i in range(1,N+1):
    prefix[i] = num_list[i-1]+prefix[i-1]
    
end = N
result = prefix[-1]
min_prefix = float('inf')
# 최댓값 계산
for end in range(1, N + 1):
    min_prefix = min(min_prefix, prefix[end - 1])  # 이전까지의 최소 prefix 값을 업데이트
    result = max(result, prefix[end] - min_prefix)  # 구간 합의 최댓값 계산

print(result)