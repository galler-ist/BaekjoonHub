def recur(num):
    if len(my_list)==M:
        print(*my_list)
        return
    
    for i in range(num, N+1):
        if i in my_list:
            continue
        my_list.append(i)
        recur(i)
        my_list.pop()

N, M = map(int,input().split())
my_list = []
recur(1)