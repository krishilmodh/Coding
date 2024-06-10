def Vowels(str):
    # normal_str = "".join(s.lower() for s in str if s.isalnum())
    vowels = "aeiouAEIOU"
    count = 0
    for i in str:
        if i in vowels:
            count += 1
    return count


result = Vowels("hello WORLD")
print("Total Vowels in string : ", result)
