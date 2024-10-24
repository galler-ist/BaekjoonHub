def rot(arr):
    vowels = ["a", "i" , "y", "e", "o", "u"]
    consonants = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]
    result=""
    for char in arr:
        temp = char.lower()
        if temp in vowels:
            new_char = vowels[vowels.index(temp)-3]
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        elif temp in consonants:
            new_char = consonants[consonants.index(temp)-10]
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += temp
    return result
            
while True:
    try:
        arr = input()
        print(rot(arr))
    except EOFError:
        break