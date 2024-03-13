def ineq(my_len):
    global now_num,min_num,max_num,num_list,arr
    if my_len==(k+1):
        nums=int(''.join(map(str,now_num)))
        min_num = min(nums,min_num)
        max_num = max(nums,max_num)
        return
    for num in range(10):
        if num_list[num]:continue
        if now_num and arr[my_len-1]==">" and now_num[-1]<num:continue
        if now_num and arr[my_len-1]=="<" and now_num[-1]>num:continue
        num_list[num]=True
        now_num.append(num)
        ineq(my_len+1)
        if now_num:now_num.pop()
        else: return
        num_list[num]=False
             
    


k = int(input())
arr = list(input().split())
min_num=10**(k+1)
max_num=0
now_num=[]
num_list=[False for _ in range(11)]
for num in range(10):
    now_num=[num]
    num_list[num]=True
    ineq(1)
    num_list[num]=False
print(max_num)
if (min_num//(10**k))==0:
    min_num="0"+str(min_num)
min_num=str(min_num)
print(''.join(min_num))