def dots(arr):
    result = 0
    
    for idx, num in enumerate(arr):
        low = idx-1
        top = idx+1
        while low>=0 and top<N:
            temp1 = num - arr[low]
            temp2 = arr[top] - num
            if temp1 == temp2:
                result+=1
                low -=1
            elif temp1 < temp2:
                low -= 1
            else:
                top +=1

    return result

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    result = dots(arr)
    print(result)