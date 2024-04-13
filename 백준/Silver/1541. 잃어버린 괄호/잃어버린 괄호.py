arr = input()
result = 0
temp = ""
giho = "+"
for num in arr:
    if num.isdigit():
        temp = temp + num
    else:
        if giho == "+":
            result += int(temp)
            temp = ""
            if num == "-":
                giho = "-"
        else:
            result -= int(temp)
            temp = ""
        
if giho == "+":
    result += int(temp)
else:
    result -= int(temp)

print(result)