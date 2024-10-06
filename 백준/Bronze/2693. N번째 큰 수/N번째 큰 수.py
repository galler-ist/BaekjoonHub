def find_third(arr):
    toparr = sorted(arr[:3])
    for num in arr[3:]:
        if num<toparr[0]:
            continue
        elif num<toparr[1]:
            toparr[0] = num
        elif num<toparr[2]:
            toparr = [toparr[1],num,toparr[2]]
        else:
            toparr = [toparr[1],toparr[2],num]
    return toparr[0]
    

t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    result = find_third(arr)
    print(result)