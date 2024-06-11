def CountWord(str):
    # count = 0
    # for i in str:
    #     count += 1
    # return count
    x= str.split()
    return len(x)

print("count", CountWord("Hello"))
