def CheckPalindrome(str):
    # no need to appent in list
    # we can use strip on string to reverse
    lst = []
    for i in str:
        lst.append(i)
    reverse = lst[::-1]
    print("reverse", reverse)
    if lst == reverse:
        print("Palindrome")
    else:
        print("Not")


CheckPalindrome("heeh")


##############################
def CheckPalindrome2(str):
    normal_str = "".join(char.lower() for char in str if char.isalnum())
    print(normal_str)
    reverse = normal_str[::-1]

    return normal_str == reverse


result = CheckPalindrome2("hellos olleh")
print("palindrome" if result else "not ")
# y = "kkr"
# r = y[::-1]
# print("R ", r)
