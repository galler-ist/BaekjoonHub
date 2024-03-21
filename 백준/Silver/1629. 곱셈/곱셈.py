def recursive(x,n,C):
    if n<=3 : return (x**n)%C
    rem = n%4

    if rem==0:
        y = recursive(x,n//4,C)
        return (y*y*y*y)%C
    elif rem==1:
        y = recursive(x,(n-1)//4,C)
        return (y*y*y*y*x)%C        
    elif rem==2:
        y = recursive(x,(n-2)//4,C)
        return (y*y*y*y*x*x)%C        
    else:
        y = recursive(x,(n-3)//4,C)
        return (y*y*y*y*x*x*x)%C        


A,B,C = map(int,input().split())
a=A%C
print(recursive(a,B,C))