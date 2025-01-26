def recur():

    if len(arr)==M:
        print(*arr)
        return
    
    for i in num_list:
        arr.append(i)
        recur()
        arr.pop()
    

N, M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))
arr=[]
recur()