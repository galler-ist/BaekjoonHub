from collections import deque
def make_one(N):
    nums = [float('inf') for _ in range(N+1)]
    num_list = deque()
    num_list.append(N)
    nums[N]=0
    while num_list:
        num = num_list.popleft()
        if num%3==0:
            num_next = num//3
            if nums[num_next]>nums[num]+1:
                nums[num_next] = nums[num]+1
                num_list.append(num_next)
            if num_next == 1:
                return nums[1]

                                 
        if num%2==0:
            num_next = num//2
            if nums[num_next]>nums[num]+1:
                nums[num_next] = nums[num]+1
                num_list.append(num_next)
            if num_next == 1:
                return nums[1]

                
        num_next = num-1
        if nums[num_next]>nums[num]+1:
            nums[num_next] = nums[num]+1
            num_list.append(num_next)
        if num_next == 1:
            return nums[1]

    return nums[1]
    
    

N = int(input())
result = make_one(N)
print(result)