def my_copy(long,short):
    result = 0
    index = 0
    while index<=(len(long)-len(short)):
        Isbreak = False
        temp_index = 0
        # 만약 short 첫 글자랑 다르다? -> result +=1, index+=1
        # 만약 short 첫 글자는 같다? -> 다시 for문을 돌리며 확인하는데, 그러다 아닌게 들통 -> 거기까지 들었던 칸을 더하기
        # 그렇게 for문을 돌다가 short 끝까지 도달했다? -> result +=1, index+=len(short)
        for alpha in long[index:index+len(short)]:
            if alpha == short[temp_index]:
                temp_index += 1
                continue
            else:
                index += 1
                result +=1
                break
        else:
            index += temp_index
            result +=1
    if index != (len(long)-len(short)):
        result += (len(long)-index)
                
    return result


t = int(input())
for _ in range(t):
    s, p = input().split()
    result = my_copy(s,p)
    print(result)