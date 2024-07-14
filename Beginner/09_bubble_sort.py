def BubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            temp = 0
            if nums[i] < nums[j]:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
    return nums


nums = [4, 2, 5, 6]
print("sorted ", BubbleSort(nums))
