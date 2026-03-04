N = int(input())
result = 0
studies = list(map(int,input().split()))
total = sum(studies) + (N-1)*8
A = total//24
B = total%24
print(A,B)