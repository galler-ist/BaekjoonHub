word = "SciComLove"
N = int(input())
new_word=word[N%10:]+word[:N%10]
print(new_word)