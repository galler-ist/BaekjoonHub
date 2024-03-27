import sys
def jeu(arr):
    global result, answer
    #TODO: 반환해야 할게 어디부터 어디까지 구매한지: index로 > return을 [s,e], 그 보석 가치의 합: my_sum으로
    #TODO: 그렇게 return 된 게 나중에 answer에 들어갈거임
    # 누적 합 계산
    prefix_sum = [0] * (L+1)
    for i in range(1,L+1):
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1] 
    #1. [0, 30, 100, 90, 100, 100]
    #2. [0, 90, 170, 240, 300, 300, 240, 240, 300, 240]
    # print(prefix_sum)
    return_sum=prefix_sum[1]
    return_list=[1,1]
    for s in range(L+1):
        for e in range(s+1,L+1):
            # my_sum = sum(arr[s:e])
            my_sum = prefix_sum[e]-prefix_sum[s]
            if my_sum>return_sum:
                return_list=[s,e]
                return_sum=my_sum
            elif my_sum==return_sum:
                if return_list[1]-return_list[0]>e-s:
                    return_list = [s,e]
    answer.append(return_list)
    result+=return_sum
    return    
    # TODO: 다 더한거는 jeu라는 함수가 완전히 다 끝날 때 result에다가 my_sum을 더함

n = int(input())
answer=[]
result=0
for _ in range(n):
    L = int(input())    #L은 보석 개수
    arr = list(map(int,input().split()))
    jeu(arr)
    # answer.append(jeu(arr))
print(result)
# print(answer)
for s,e in answer:
    if s>=e:
        print(e,e)
    else:
        print(s+1, e)
    