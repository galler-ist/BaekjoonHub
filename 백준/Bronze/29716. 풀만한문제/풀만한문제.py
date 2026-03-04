def question(weeds, J):
    volume = 0
    for word in weeds:
        if word.isupper():
            volume += 4
        elif word.islower() or word.isdigit():
            volume += 2
        else:
            volume += 1
    if volume<=J:
        return True
    else:
        return False

J,N = map(int,input().split())
result = 0
for _ in range(N):
    weed_list = list(input().strip())
    result += question(weed_list,J)
print(result)