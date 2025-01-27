def check_box(books):
    result = 0
    temp = 0
    for book in books:
        temp += book
        if temp>M:
            result +=1
            temp = book
    if temp!=0:
        result+=1

    return result

N, M = map(int,input().split())
if N:
    books = list(map(int,input().split()))
    result = check_box(books)
else:
    result = 0
print(result)