def leaders(nums):
    result = []
    for num in range(len(nums)-1):
        if nums[num] > max(nums[num+1:]):
            result.append(nums[num])
    result.append(nums[-1])
    return result

print(leaders([10, 22, 12, 3, 0, 6]))