a,b,c,m = map(int,input().split())
result = 0
time = 0
stress = 0
while time<=23:
    if stress + a > m:
        time+=1
        stress -= c
        stress = max(0,stress)
    else:
        stress += a
        result += b
        time+=1
print(result)