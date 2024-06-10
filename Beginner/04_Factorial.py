def Factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        num = Factorial(num - 1) * num
    return num


result = Factorial(5)
print("factorial: ", result)

#  alternative"


def Factorial2(num2):
    # if num2 == 1 or num2 == 0:
    #     return 1
    # else:
    t = 1
    for i in range(1, num2+1):
        t = t * i
    return t


result2 = Factorial2(5)
print("factorial: ", result2)
