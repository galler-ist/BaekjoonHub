def check_box(j,boxes):
    count = 0
    sum = 0
    for vol in boxes:
        count +=1
        sum += vol
        if sum >=j:
            return count
T = int(input())
for _ in range(T):
    j, N = map(int,input().split())
    boxes = []
    for _ in range(N):
        r,c = map(int,input().split())
        boxes.append(r*c)
    boxes.sort(reverse=True)
    print(check_box(j,boxes))