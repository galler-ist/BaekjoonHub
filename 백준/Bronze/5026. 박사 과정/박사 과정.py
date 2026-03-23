N = int(input())
for _ in range(N):
    ques = list(input().split('+'))
    if ques[0]=="P=NP":
        print("skipped")
    else:
        print(int(ques[0])+int(ques[-1]))