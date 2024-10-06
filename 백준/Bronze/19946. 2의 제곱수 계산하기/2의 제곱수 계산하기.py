import math
num = int(input())
result = int(math.log2(18446744073709551616-num))
print(64-result)