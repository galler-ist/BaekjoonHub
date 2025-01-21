def divisor(A,B):
    final = B//A
    # 이제 final의 모든 약수를 구해보자!
    div_list = []
    for i in range(1,int(final**0.5) + 1):
        if final%i==0:
            div_list.append(i)
            div_list.append(final//i)
    div_list= sorted(div_list)
    div_len = len(div_list)
    
    # 하고나서, 2개의 공약수가 1이 아니라면 다시 index 바꾸기!
    mid = div_len//2
    idx = 1
    if div_len%2==0:
        first, second = div_list[mid -idx], div_list[mid+idx-1]
        while first>=1:
            first, second = div_list[mid -idx], div_list[mid+idx-1]
            if gcd(first,second)==1:
                return A*first, A*second
            idx+=1
    else:
        first, second = div_list[mid -idx], div_list[mid+idx]
        while first>=1:
            first, second = div_list[mid -idx], div_list[mid+idx-1]
            if gcd(first,second)==1:
                return A*first, A*second
            idx+=1
    return A*first, A*second

    
def gcd(a,b):
    while a%b != 0:
        tmp = a%b
        a = b
        b = tmp
    return b
        

A,B = map(int,input().split())
result1, result2 = divisor(A,B)
print(result1, result2)
