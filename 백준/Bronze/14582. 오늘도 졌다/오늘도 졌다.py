def result(t1,t2):
    score=0
    for i in range(9):
        if score+t1[i]>0:
            return "Yes"
        score += (t1[i]-t2[i])
    return "No"

myteam = list(map(int,input().split()))
opteam = list(map(int,input().split()))
print(result(myteam,opteam))