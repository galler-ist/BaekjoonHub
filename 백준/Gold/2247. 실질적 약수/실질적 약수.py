import sys

input = sys.stdin.readline

def csod(n):
    result = 0
    if n <= 3: 
        return result
    
    sqrtn = int(n**0.5)
    for num in range(2, sqrtn + 1):
        k = n // num
        result += num * (k - num + 1) + (k - num) * (k + num + 1) // 2
        result %= 1000000

    return result

n = int(input())
result = csod(n)
print(result)