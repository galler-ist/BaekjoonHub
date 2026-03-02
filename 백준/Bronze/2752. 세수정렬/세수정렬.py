a,b,c = map(int,input().split())
num1, num2, num3 = 0,0,0
num1 = min(a,b,c)
num3 = max(a,b,c)
num2 = a+b+c-num1-num3
print(num1,num2,num3)