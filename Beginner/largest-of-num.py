a = 10
b = 20
c = 35


def LargestOfNum(a, b, c):
    if a >= b and a >= c:
        return print("a is largest", a)
    elif b >= a and b >= c:
        return print("b is largest", b)
    else:
        return print("c is largest", c)


LargestOfNum(a, b, c)
