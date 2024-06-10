def SecondLargest(nums):
    max = 0
    lst = []
    for num in nums:
        if num > max:
            max = num
            lst.append(max)
        x= len(lst)
    return    lst[x-2]


nums = [10, 20, 4, 45, 99]
print(SecondLargest(nums))
