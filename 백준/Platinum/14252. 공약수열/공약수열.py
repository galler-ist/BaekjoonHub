def gcdlist(nums):
    count = 0
    idx = 0
    length = len(nums)
    nums = sorted(nums)
    while idx<=length-2:
        A = nums[idx]
        B = nums[idx+1]
        if gcd(A,B)!=1:
            count += check_gcd(A,B)
        idx+=1
    return count


def check_gcd(a,b):
    for i in range(a,b):
        if gcd(a,i)==1:
            if gcd(b,i)==1:
                return 1
    return 2
        
def gcd(a,b):
    while a%b!=0:
        temp = a%b
        a=b
        b=temp
    return b


N = int(input())
nums = list(map(int,input().split()))
print(gcdlist(nums))