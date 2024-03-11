import sys
R,C = map(int,input().split())
arr=[list(sys.stdin.readline()) for _ in range(R)]
words=[]
#garo
for j in range(R):
    word=""
    for i in range(C):
        if arr[j][i]!="#":
            word = word + arr[j][i]
        else:
            if len(word)>=2:
                words.append(word)
            word=""
    if len(word)>=2:
        words.append(word)
#sero
for i in range(C):
    word=""
    for j in range(R):
        if arr[j][i]!="#":
            word = word + arr[j][i]
        else:
            if len(word)>=2:
                words.append(word)
            word=""
    if len(word)>=2:
        words.append(word)
        
words.sort()
print(words[0])