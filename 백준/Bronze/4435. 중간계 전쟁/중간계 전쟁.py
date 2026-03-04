g_list=[1,2,3,3,4,10]
s_list = [1,2,2,2,3,5,10]
N = int(input())
for battle in range(N):
    gandalfs = list(map(int,input().split()))
    result1 = sum(g_list[i]*gandalfs[i] for i in range(6))
    saurons = list(map(int,input().split()))
    result2 = sum(s_list[i]*saurons[i] for i in range(7))
    if result1>result2:
        sentence = "Good triumphs over Evil"
    elif result1<result2:
        sentence = "Evil eradicates all trace of Good"
    else:
        sentence = "No victor on this battle field"
    print(f"Battle {battle+1}: {sentence}")