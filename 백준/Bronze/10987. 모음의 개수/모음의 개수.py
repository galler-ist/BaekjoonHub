def check_vowel(str):
    if str in ["a","e","i","o","u"]:
        return True
    else : return False

answer = 0
string = input()
for str in string:
    answer += check_vowel(str)
print(answer)