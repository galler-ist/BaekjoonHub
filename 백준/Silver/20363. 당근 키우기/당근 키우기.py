X,Y = map(int,input().split())
result = 0
if X>=Y:
    result = X+Y+Y//10
else:
    result = Y+X+X//10
print(result)