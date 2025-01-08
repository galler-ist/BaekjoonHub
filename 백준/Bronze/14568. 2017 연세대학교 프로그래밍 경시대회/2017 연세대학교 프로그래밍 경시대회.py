result = 0
N = int(input())
for a in range(2,N,2):
    for b in range(1,N-a):
        if N-a-b>=b+2:
            result+=1
        else:
            break
print(result)