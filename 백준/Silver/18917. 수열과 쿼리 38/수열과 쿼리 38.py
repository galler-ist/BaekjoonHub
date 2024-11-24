import sys
input = sys.stdin.readline
M = int(input())
mysum = 0
xor = 0
for _ in range(M):
    query = list(map(int,input().split()))
    if query[0]==1:
        mysum += query[1]
        xor = xor^query[1]
    elif query[0]==2:
        mysum -= query[1]
        xor = xor^query[1]
    elif query[0] == 3 : print(mysum)
    elif query[0] == 4 : print(xor)