import sys

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
team_list= [False for _ in range(N+1)]
team1=[]
result=float('inf')

def soccerteam(team1):
    global team_list,result
    #TODO: 만약 team1의 길이가 N//2라면 team_list에서 False인 부분들은 team2에 넣기
    #TODO: 또 다른 함수에서 두 팀의 능력치 차이를 계산해서 값으로 받고, result와 비교
    if len(team1)==N//2:
        team2=[]
        for index,value in enumerate(team_list):
            if index==0:continue
            if not value:
                team2.append(index)
        score=ability(team1,team2)
        result = min(result, score)
        return
            
    for mem in range(1,N+1):
        if team_list[mem]:continue
        if not team1 or mem > team1[-1]:
            team_list[mem]=True
            team1.append(mem)
            soccerteam(team1)
            team1.pop()
            team_list[mem]=False
    return

def ability(t1,t2):
    #TODO: team1에 대해서 먼저하기

    t1a = sum(arr[i-1][j-1] + arr[j-1][i-1] for i in t1 for j in t1 if i != j)
    t2a = sum(arr[i-1][j-1] + arr[j-1][i-1] for i in t2 for j in t2 if i != j)
    return abs(t1a-t2a)
    
soccerteam([])
print(result//2)