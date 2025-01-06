
def check_nova(novas):
    n_c, n_t = 0, -100
    for i in range(len(novas)):
        if novas[i]>=n_t+100:
            n_c +=1
            n_t = novas[i]
    return n_c

def check_origin(origins):
    o_c, o_t = 0, -360
    for i in range(len(origins)):
        if origins[i]>=o_t+360:
            o_c +=1
            o_t = origins[i]
    return o_c

# N, M : 에르다노바, 오리진
N, M = map(int,input().split())

novas = list(map(int,input().split()))
novas = sorted(novas)
origins = list(map(int,input().split()))
origins = sorted(origins)

result1 = check_nova(novas)
result2 = check_origin(origins)

print(result1, result2)