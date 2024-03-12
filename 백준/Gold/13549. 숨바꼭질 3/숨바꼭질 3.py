from collections import deque

def hide(N):
    stack = deque()
    stack.append([N,0])
    person_list= [float('inf') for _ in range(150001)]
    person_list[N]=0
    while stack:
        d,t = stack.popleft()
        if d<0 or d>=150000:continue
        if person_list[d-1]>t+1:
            person_list[d-1]=t+1
            stack.append([d-1,t+1])    
        if person_list[d+1]>t+1:
            person_list[d+1]=t+1
            stack.append([d+1,t+1])     
        if d<=66667 and person_list[2*d]>t:
            person_list[2*d]=t
            stack.append([2*d,t])

    return person_list

N,K = map(int,input().split())
result=hide(N)
print(result[K])