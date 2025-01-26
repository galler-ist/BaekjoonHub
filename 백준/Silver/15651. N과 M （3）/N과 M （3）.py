def recur():

    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(1,N+1):
        arr.append(i)
        recur()
        arr.pop()
    

N, M = map(int,input().split())
arr=[]
recur()