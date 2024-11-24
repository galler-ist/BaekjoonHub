import sys
# max_dp와 min_dp에다가 그냥 첫 번째 list를 적는다!
# 이후 stairs 라는 리스트를 N-1만큼 반복해서 입력 받는다!


input = sys.stdin.readline

N = int(input())
first_scores = list(map(int,input().split()))

max_dp = first_scores
min_dp = first_scores

for _ in range(N-1):
    scores = list(map(int,input().split()))
    max_dp = [(max(max_dp[0],max_dp[1])+scores[0]),(max(max_dp[0],max_dp[1],max_dp[2])+scores[1]),(max(max_dp[1],max_dp[2])+scores[2])]
    min_dp = [(min(min_dp[0],min_dp[1])+scores[0]),(min(min_dp[0],min_dp[1],min_dp[2])+scores[1]),(min(min_dp[1],min_dp[2])+scores[2])]

print(max(max_dp), min(min_dp))