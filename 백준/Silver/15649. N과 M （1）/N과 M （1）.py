def make_seq(N,M,my_list):
    if len(my_list)==M:
        print(*my_list)
        return
    for num in range(1,N+1):
        if num in my_list:
            continue
        my_list.append(num)
        make_seq(N,M,my_list)
        my_list.pop()
    return
        
    

N,M = map(int,input().split())
make_seq(N,M,[])