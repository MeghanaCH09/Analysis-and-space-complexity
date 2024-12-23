def printer(n):
    if (n==0 or n==1):
        return 1
    return n*printer(n-1)
print()
