def time_money(hands, K):
    count = 0
    for _ in range(M):
        count += hands[_]
        if count >= K:
            return _+1
    return 101
        
hand_N, hand_M = 0,101
N, M, K = map(int,input().split())
for person in range(N):
    hands = list(map(int,input().split()))
    temp_M = time_money(hands, K)
    if hand_M > temp_M:
        hand_M = temp_M
        hand_N = person+1
print(hand_N, hand_M)