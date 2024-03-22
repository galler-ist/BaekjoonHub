def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

def find_num(num):
    s=0
    e=n-1
    while s<=e:
        m=(s+e)//2
        if arr[m]<num:
            s=m+1
        elif arr[m]>num:
            e=m-1
        else:
            return (m)*(n-m-1)
    return 0


n,q = map(int,input().split())
arr = list(map(int,input().split()))
arr=(merge_sort(arr))
for _ in range(q):
    mi=int(input())
    print(find_num(mi))