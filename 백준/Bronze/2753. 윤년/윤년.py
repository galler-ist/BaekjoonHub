year=int(input())
a=0
if year%4==0:
    a=1
    if year%100==0:
        a=0
        if year%400==0:
            a=1
print(a)