import sys
# 스스로가 마니또거나 마니또가 없는 사람은 없음
#TODO: student_list와 manito_list를 만들거고, 인덱스는 1부터 시작할거임
N,M = map(int,input().split())
student_list = [False] * (N+1)
manito_list = [False] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())  #TODO: a번 학생의 마니또가 b번 학생
    manito_list[a]=True             #TODO: manito_list는 마니또 당하는애, student_list는 마니또 하는애
    student_list[b]=True
s = int(input())    #세종이의 번호, 세종이의 마니또 후보가 누구일지 맞추기
#student_list[1:]에서 False의 갯수 찾기, but 본인 인덱스 빼기 > False가 1이하면 NOJAM, 그 이상이면 그 개수 출력
#만약 manito_list[s]가 True라면 NOJAM

def manito():
    result=0
    nofriend=0
    if manito_list[s]:return "NOJAM"
    
    for i in range(1,N+1):
        if not student_list[i] and i!=s:
            result+=1
        if student_list[i]==manito_list[i]==False:nofriend+=1
        
    if result<=2 and nofriend==1:return "NOJAM"
    if result<=1:return "NOJAM"
    return result

print(manito())