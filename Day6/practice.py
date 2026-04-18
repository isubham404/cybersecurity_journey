def myFunc(n) :
    return abs(n-50)

a = [100, 25 , 45 , 35 ,20]
a.sort(key=myFunc)
print(a)
