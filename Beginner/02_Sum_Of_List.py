def SumOfList(nums):
    sum = 0
    x = len(nums)
    for i in range(x):
        sum += nums[i]
    return print("sum : ", sum)

SumOfList([1, 2, 3, 4, 5])

##########################################

def SumOfList2(nums):
    sum = 0
    for num in nums:
        sum += num
    return print("sum", sum)

SumOfList2([1, 2, 3, 4, 5])
