def check_box(books):
    result = 1
    temp = 0
    for book in books:
        if book+temp<=M:
            temp+=book
        else:
            result +=1
            temp = book
    return result

N, M = map(int,input().split())
if N:
    books = list(map(int,input().split()))
    result = check_box(books)
else:
    result = 0
print(result)