def recur(num):

    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(num,N+1):
        arr.append(i)
        recur(i)
        arr.pop()
    

N, M = map(int,input().split())
arr=[]
recur(1)