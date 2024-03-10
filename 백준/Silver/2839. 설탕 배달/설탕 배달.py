N=int(input())
p5=N//5
p3=0
my_sum=0
while p5>=0:
    my_sum=p5*5+p3*3
    while my_sum<N:
        p3+=1
        my_sum=p5*5+p3*3
    if my_sum==N: result=p5+p3; break
    p5-=1
    p3=0
result=p5+p3
print(result if result else -1)