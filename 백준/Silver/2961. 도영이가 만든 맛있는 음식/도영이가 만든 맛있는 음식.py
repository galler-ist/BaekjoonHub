def recur(idx, S, B):
    global answer
    if idx==N:
        if S==1 and B==0:
            return
        temp = abs(S-B)
        answer = min(temp,answer)
        return

    recur(idx+1,S*ingre[idx][0], B+ingre[idx][1])
    recur(idx+1,S, B)
    
N = int(input())
ingre = [list(map(int,input().split())) for _ in range(N)]
answer = float('inf')
recur(0,1,0)
print(answer)