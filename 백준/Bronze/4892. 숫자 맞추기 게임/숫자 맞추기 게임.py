n = 1
while True:
    a = int(input())
    if a==0 : break
    if a%2:
        mystr="odd"
        print(f"{n}. {mystr} {(a-1)//2}")
    else :
        mystr="even"
        print(f"{n}. {mystr} {a//2}")
    n += 1
    
