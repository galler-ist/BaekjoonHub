from collections import deque
croatia=["c=","c-","d-","lj","nj","s=","z="]
pick_list = ["c","d","l","n","s","z"]
q=deque(input())
result = 0
while q:
    s = q.popleft()
    if s in pick_list and q:
        ns = q[0]
        if s=="d" and ns=="z" and len(q)>=2:      #dz=는 따로
            nns = q[1]
            if nns=="=":
                q.popleft()
                q.popleft()
        elif (s+ns) in croatia:
            q.popleft()
    result+=1
print(result)