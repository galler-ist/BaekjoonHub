def right_arr(arr):
    open = 0
    close = 0
    for round in arr:
        if round == '(':
            open+=1
        else:
            close+=1
        if close>open:
            return "NO"
    if open!=close:
        return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    arr = input()
    result = right_arr(arr)
    print(result)