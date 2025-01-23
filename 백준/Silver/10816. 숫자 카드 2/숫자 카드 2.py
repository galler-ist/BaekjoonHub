n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

cnt_list = [0 for _ in range(10000000*2+1)] # (idx+ 10000000)


for num in n_list:
    cnt_list[num+10000000] +=1
for num in m_list:
    print(cnt_list[num+10000000],end=' ')