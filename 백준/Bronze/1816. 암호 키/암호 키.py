def check_num(num):
    for temp in range(2,1000000):
        if num%temp ==0 :
            return "NO"
    return "YES"
        

N = int(input())
for _ in range(N):
    num = int(input())
    result = check_num(num)
    print(result)