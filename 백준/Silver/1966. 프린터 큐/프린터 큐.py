import sys
from collections import deque
T = int(input())
def document(doc_list,M):
    global result
    while doc_list:
        doc,idx = doc_list.popleft()    
        reroll=False
        for other in doc_list:
            if other[0]>doc:
                doc_list.append([doc,idx])
                reroll=True
                break
            else:
                continue
        if not reroll:
            if idx==M:return
            result+=1
for tc in range(1,T+1):
    N,M=map(int,input().split())    #TODO: N:문서의개수, M:몇 번째로 인쇄되었는지 궁금한 문서가 큐에서 몇 번째에 있는지
    queue=deque()
    important_list=list(map(int,input().split()))
    for index,num in enumerate(important_list):
        queue.append([num,index])
    result=1   
    document(queue,M) 
    # queue = deque((map(int,input().split())))  #TODO: N개 문서의 중요도
    print(result)
        
    
    
    
    
    
