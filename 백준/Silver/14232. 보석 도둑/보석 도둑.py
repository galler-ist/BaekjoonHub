N = int(input())
answer_list = []
num=N
temp =2

while temp<=(num**(0.5)):
    if num%temp==0:
        answer_list.append(temp)
        num = num//temp
    else:
        temp+=1
if num!=1:
    answer_list.append(num)
print(len(answer_list))
answer_list=sorted(answer_list)
print(" ".join(map(str,answer_list)))