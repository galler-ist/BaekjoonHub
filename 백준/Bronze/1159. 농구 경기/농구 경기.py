first = {}
answer = []
n = int(input())
for _ in range(n):
    names = input()
    first_str = names[0]
    if first_str in first:
        first[first_str] += 1
    else :
        first[first_str] = 1
for name in first:
    if first[name]>=5:
        answer.append(name)
if not answer:
    result = "PREDAJA"
else:
    answer = sorted(answer)
    result = "".join(answer)
print(result)
