# (2,2), (1,1), (0,0) <- 2행
# (2,1), (1,0) <- 1행
# (2,0) <- 0행

def check(A1,A2,A3,A4,A5,A6,B):
    num1, num2, num3, num4, num5, num6 = 0,0,0,0,0,0
    for j in range(N):
        for i in range(j+1):
            if A1[j][i] != B[j][i] :
                num1 +=1
            if A2[j][i] != B[j][i] :
                num2 +=1            
            if A3[j][i] != B[j][i] :
                num3 +=1            
            if A4[j][i] != B[j][i] :
                num4 +=1
            if A5[j][i] != B[j][i] :
                num5 +=1
            if A6[j][i] != B[j][i] :
                num6 +=1
    return min(num1,num2,num3,num4,num5,num6)
                
                
def make_60(lst):
    new_list=[]
    for num in range(N):
        temp = []
        j, i = N-1, num
        while i >=0 :
            temp.append(lst[j][i])
            j -=1
            i -=1
        new_list.append(temp)
    return new_list

def make_symmetry(lst):
    new_list = []
    for num in range(N):
        temp = []
        for num2 in range(num,-1,-1):
            temp.append(lst[num][num2])
        new_list.append(temp)
    return new_list

N = int(input())
A = []
B = []
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))

A_60 = make_60(A)
A_120 = make_60(A_60)
A_sym = make_symmetry(A)
A_60_sym = make_symmetry(A_60)
A_120_sym = make_symmetry(A_120)
print(check(A,A_60,A_120,A_sym,A_60_sym,A_120_sym,B))