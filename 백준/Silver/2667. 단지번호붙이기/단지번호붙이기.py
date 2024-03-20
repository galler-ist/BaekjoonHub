import sys
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def danzi(y,x):
    global arr,k
    
    for dir in directions:
        ny,nx = y+dir[0], x+dir[1]
        if ny<0 or nx<0 or ny>=N or nx>=N:continue
        if arr[ny][nx]==1:
            arr[ny][nx]=k
            danzi(ny,nx)  
    return


N = int(input())
arr= [list(map(int,input())) for _ in range(N)]
#TODO: 먼저 arr을 돌며 1을 만나면
j=i=0
k=2
for j in range(N):
    for i in range(N):
        if arr[j][i]==1:
            arr[j][i]=k
            danzi(j,i)
            k+=1
klist=[0]*(k)
for K in range(1,k+1):
    for j in range(N):
        for i in range(N):
            if arr[j][i]==K:
                klist[K]+=1
print(k-2)
answer=sorted(klist[2:])
for _ in answer:
    print(_)
    