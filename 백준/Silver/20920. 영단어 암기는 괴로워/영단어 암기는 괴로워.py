import sys

# TODO: 1.자주 나오면 앞 > 2. 길이가 길면 앞 > 3. 사전 순
# TODO: 우선 M이 안 되면 cut!

word_list = {}
N, M = map(int,sys.stdin.readline().split()) # N:단어 개수, M: 최소 길이 수
for _ in range(N):
    word = input()
    if len(word)>=M:
        # word_list에 있냐?
        if word in word_list:
            word_list[word][0]+=1
        else:
            word_list[word] = [1,len(word)]
def my_sort(item):
    return (-item[1][0], -item[1][1], item[0])

new_list = sorted(word_list.items(), key = my_sort)
for key in new_list:
    print(key[0])