def bubble_sort(A,K,my_list):
    result = 0
    for j in range(A,0,-1):
        for i in range(j-1):
            if my_list[i]>my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                result +=1
                if result ==K :
                    print(*my_list)
                    return
    print(-1)
    return
    



A,K = map(int,input().split())
my_list = list(map(int,input().split()))
bubble_sort(A,K,my_list)