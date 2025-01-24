def make_balls(num):
    global baseballs, baseball
    if len(baseball)==3:
        temp = int(baseball[0]*100+baseball[1]*10+baseball[2])
        baseballs.append(temp)
        return
            
    for i in range(1,10):
        if i in baseball:
            continue
        baseball.append(i)
        make_balls(num+1)
        baseball.pop()
        
def num_baseball(num):
    global answer
    num_str = str(num)
    for yeongsu in baseball_list:
        n,s,b = yeongsu
        strike,ball = 0,0
        for i in range(3):
            if num_str[i]==n[i]:
                strike+=1
            elif num_str[i] in n:
                ball+=1
        
        if s==strike and b==ball:
            continue
        else:
            return
    
    answer += 1
    return
            
                
            


baseball_list = []
N = int(input())
for _ in range(N):
    num,strike,ball = input().split()
    strike = int(strike)
    ball = int(ball)
    baseball_list.append([num,strike,ball])
baseballs = []
baseball = []
make_balls(1)
answer = 0
for idx in range(len(baseballs)):
    num_baseball(baseballs[idx])
    

print(answer)