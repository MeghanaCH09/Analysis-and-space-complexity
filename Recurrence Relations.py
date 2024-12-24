#Function 1
def myfunction(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Congingal")
    myfunction(n/2)
    myfunction(n/3)

#Function 2
def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)

#Print Recurrnece Relations
print("For the first function:")
print("T(n) = T(n-1) + T(n.3) + N")
print()
print("For the second function:")
print("T(n) = T(n-1) + 1")