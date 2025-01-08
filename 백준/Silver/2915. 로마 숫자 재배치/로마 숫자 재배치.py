def change_roma(roma):
    if roma[:2]== "LX" and roma[:3] != "LXX":
        roma = roma.replace("LX", "XL")

    if len(roma)>=2 and roma[-2:]=="XI":
        roma = roma.replace("XI", "IX")
        
    if roma[:2]== "LX" and roma[:3] != "LXX":
        roma = roma.replace("LX", "XL")
        
        
    word = None
    for i in range(len(roma)):
        if roma[i]== "V" or roma[i]== "I":
            word = i
            break
    if word >=0:
        if roma[word:] == "VI":
            roma = roma.replace("VI", "IV")
            
    return roma          

# 만약 LXXI(71) 인경우 2번째인 LXIX(69)로 바꾸고, 다시 XLIX(49)로 바꿔야 하기때문문 
# VI -> IV ; 6 -> 4
# XI -> IX ; 11 -> 9 / 다른 경우도 가능
# LX -> XL ; 60 -> 40
roma = input()

result = change_roma(roma)

print(result)