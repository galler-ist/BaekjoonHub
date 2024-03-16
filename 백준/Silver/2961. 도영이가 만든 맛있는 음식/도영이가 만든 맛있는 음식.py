import sys

def food(selected):
    global result
    sour=1
    bitter=0
    if not selected:return
    for s,b in selected:
        sour*=s
        bitter+=b
    result = min(result,abs(sour-bitter))
    return

def make_selected(arr):
    result_list=[]
    for i in range(1<<N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])
        result_list.append(subset)
    return result_list


N = int(input())
#TODO: 신 맛은 사용한 재료의 신맛의 곱, (앞)
#TODO: 쓴 맛은 사용한 재료의 쓴맛의 합 (뒤)
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = float('inf')
selected = make_selected(arr)
#TODO: selected를 만들기
#TODO: selected 하나하나 탐색하기
for select in selected:
    food(select)
print(result)