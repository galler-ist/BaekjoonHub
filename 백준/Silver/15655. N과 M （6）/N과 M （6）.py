def recur():

    if len(arr)==M:
        print(*arr)
        return
    
    for i in num_list:
        if i in arr:
            continue
        if arr and i<arr[-1]:
            continue
        arr.append(i)
        recur()
        arr.pop()
    

N, M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
arr=[]
recur()