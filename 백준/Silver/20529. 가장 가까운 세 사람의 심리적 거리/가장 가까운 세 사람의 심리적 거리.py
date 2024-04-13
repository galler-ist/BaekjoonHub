T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mbti = list(input().split())
    friends_list=[]
    result = 20
    if N>=33:
        result=0
    else:
        for j in range(len(mbti)):
            for k in range(j+1,len(mbti)):
                for l in range(k+1,len(mbti)):
                    p1,p2,p3 = mbti[j],mbti[k],mbti[l]
                    if [p1,p2,p3] in friends_list:continue
                    friends_list.append([p1,p2,p3])
                    temp = 0
                    for i in range(4):
                        if p1[i]!=p2[i]:
                            temp+=1
                        if p1[i]!=p3[i]:
                            temp+=1
                        if p2[i]!=p3[i]:
                            temp+=1
                        if temp > result : break
                    result = min(temp,result)
    print(result)