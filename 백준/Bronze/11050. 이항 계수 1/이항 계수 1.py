def bino(N,K):
    result = 1
    divide = 1
    while K>=1:
        result *= N
        divide *= K
        N -= 1
        K -=1
    return int(result/divide)
N, K = map(int,input().split())
if K==0:
    print(1)
else:
    print(bino(N,K))
