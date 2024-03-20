def dis(x1,y1,r1,x2,y2,r2):
    r=(((x1-x2)**2+(y1-y2)**2)**0.5)
    #TODO: 두 좌표가 같을 때!
    if [x1,y1]==[x2,y2]:
        if r1==r2==0: return 1
        elif r1==r2: return -1
        else : return 0
    
    if r1+r2>r and r1+r>r2 and r2+r>r1: return 2
    elif r1+r2==r or r1+r==r2 or r2+r==r1: return 1
    else : return 0

T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    print(dis(x1,y1,r1,x2,y2,r2))