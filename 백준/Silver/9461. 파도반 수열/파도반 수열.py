def pado(n):
    global nums
    if nums[n]==0:
        nums[n]=pado(n-2)+pado(n-3)
    return nums[n]
T = int(input())
for _ in range(T):
    N = int(input())
    nums=[0 for _ in range(101)]
    nums[1]=nums[2]=nums[3]=1
    result=pado(N)
    print(result)