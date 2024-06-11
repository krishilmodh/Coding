def RemoveDuplicate(nums):
    x = len(nums)
    lst = []
    for i in range(x):
        for j in range(x - 1):
            if nums[i] != nums[j]:
                lst.append(nums[i])

    return lst


print("new list", RemoveDuplicate([1, 2, 1, 3, 5]))
