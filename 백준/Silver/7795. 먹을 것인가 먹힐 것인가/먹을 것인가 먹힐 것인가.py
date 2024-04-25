def food(A_list,B_list):
    # [1,1,3,7,8], [1,3,6]
    # [2, 7, 13] [11, 103, 215, 290]
    # [1,1,3,7,8], [1,3,6,7,10]
    #TODO: 2개의 리스트는 이미 정렬되어있음
    #TODO: 투포인터로 진행
    #TODO: start를 굳이 쓸 필요가 없음!
    result = 0
    end = 0
    for A in A_list:
        while end<=M-1 and A>B_list[end]:
            end+=1
        result += end
    return result
    



T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())     # A의 수 : N, B의 수 : M
    A_list = sorted(list(map(int,input().split())))     # A의 크기
    B_list = sorted(list(map(int,input().split())))     # B의 크기
    print(food(A_list,B_list))