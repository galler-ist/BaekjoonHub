import sys
input = sys.stdin.readline

def sequence(N):      
    array = [True for i in range(N+1)]
    
    for i in range(2,int(N**(0.5))+1):
        if array[i]==True:
            j=2
            while i*j<=N:
                array[i*j] = False
                j +=1 
    
    return array


N, M = map(int,input().split())
result_list = sequence(N)
sum_list = [0 for i in range(N+1)]
for i in range(1,N+1):
    sum_list[i] = sum_list[i-1] + result_list[i]
for _ in range(M):
    a,b = map(int,input().split())
    result = sum_list[b]-sum_list[a-1]
    print(result)