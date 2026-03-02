n = int(input())
for a in range(n):
    k = n-a
    if a>0:
        print(" "*(a-1),"*"*(2*k-1))
    else:
        print("*"*(2*k-1))
for b in range(1,n):
    if b<n-1:
        print(" "*(n-b-2),"*"*(2*b+1))
    else:
        print("*"*(2*b+1))