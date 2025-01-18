def second_find(num):
    i=1
    answer = num
    while num>=2**i:
        answer+= (num//(2**i))*(2**(i-1))
        i+=1
    return answer


import sys
input = sys.stdin.readline
A,B = map(int,input().split())
result = second_find(B)-second_find(A-1)
print(result)
