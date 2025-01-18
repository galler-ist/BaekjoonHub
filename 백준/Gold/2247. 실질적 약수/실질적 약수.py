import sys
input = sys.stdin.readline
def sod(n):
    result = 0
    if n<=3: return result
    for num in range(2, (n//2)+1):
        result += (n//num)*num

    result -= ((n//2)*(n//2+1))//2
    result += 1
    return result%1000000

n = int(input())
result = sod(n)
print(result)