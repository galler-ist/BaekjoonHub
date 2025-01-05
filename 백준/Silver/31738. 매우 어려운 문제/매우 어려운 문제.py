def facnum(N,M):
    if N>=M:
        return 0
    result = 1
    for num in range(1,N+1):
        result *= num
        result %= M
    return result%M

N, M = map(int,input().split())
print(facnum(N,M))