def Factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        num = Factorial(num - 1) * num
    return num

result = Factorial(5)
print("factorial: ", result)
