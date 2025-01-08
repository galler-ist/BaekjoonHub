def change_list(list1, y, x):
    for yy in range(y,y+3):
        for xx in range(x,x+3):
            if list1[yy][xx]=="1":
                list1[yy][xx]="0"
            else:
                list1[yy][xx]="1"
    return list1
            

def check_matrix(list1, list2):
    cnt = 0
    if N<=2 or M<=2 :
        if list1 == list2:
            return 0
        return -1
    
    for y in range(N-2):
        for x in range(M-2):
            if list1[y][x] != list2[y][x]:
                cnt += 1
                list1 = change_list(list1, y, x)
    
    if list1 == list2:
        return cnt
    else:
        return -1
                


N, M = map(int,input().split())
list1 = []
list2 = []
for _ in range(N):
    temp = list(input())
    list1.append(temp)
    
for _ in range(N):
    temp = list(input())
    list2.append(temp)    



result = check_matrix(list1, list2)
print(result)