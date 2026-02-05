def myF(x):
    return abs(x - 50)
list = [100, 50, 85, 56, 49]
list.sort(key = myF)
print(list)