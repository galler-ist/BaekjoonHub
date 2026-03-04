import math
strokes= [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
asciiA=ord('A')
def compa(A,B):
    length = len(A)
    first = 0
    for i in range(length):
        if (i+1) == length:
            first+= strokes[ord(A[i])-asciiA]
        else:
            first += strokes[(ord(A[i])-asciiA)]*math.comb(2*length-2,i*2) + strokes[(ord(B[i])-asciiA)]*math.comb(2*length-2,i*2+1)
    second = 0
    for i in range(length):
        if (i+1) == length:
            second+= strokes[ord(B[i])-asciiA]
        else:
            second += strokes[(ord(B[i])-asciiA)]*math.comb(2*length-2,i*2) + strokes[(ord(A[i+1])-asciiA)]*math.comb(2*length-2,i*2+1)
    print(f"{first%10}{second%10}")
A = list(input())
B = list(input())
compa(A,B)