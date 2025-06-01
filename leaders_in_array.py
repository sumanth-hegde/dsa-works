def leaders(nums):
    i, maxi, result = 0, nums[0], []
    while i < len(nums)-1:
        if nums[i] > max(nums[i+1:]):
            result.append(nums[i])
        i += 1
    result.append(nums[-1])
    return result

print(leaders([10, 22, 12, 3, 0, 6]))