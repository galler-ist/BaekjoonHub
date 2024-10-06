
def pan_check(alphas,nums):
    alpha_number=0
    for idx, alpha in enumerate(alphas): # A:65~ Z:90 , -65해주기
        alpha_number += (26**(2-idx))*(ord(alpha)-65)
    nums = int(nums)
    if abs(alpha_number-nums)<=100:
        return "nice"
    else:
        return "not nice"


n = int(input())
for _ in range(n):
    pan = input()
    alphas,nums = pan.split('-')
    result = pan_check(alphas,nums)
    print(result)
