def Fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [1]
    elif num == 2:
        return [0, 1]

    lst = [0, 1]
    for i in range(2, num):
        lst.append(lst[i - 2] + lst[i - 1])
    return lst


result = Fibonacci(5)
print("fibonacci : ", result)
