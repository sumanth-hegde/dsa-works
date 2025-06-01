""" Brute force method """

def leaders(nums):
    result = []
    for num in range(len(nums)-1):
        if nums[num] > max(nums[num+1:]):
            result.append(nums[num])
    result.append(nums[-1])
    return result

print(leaders([10, 22, 12, 3, 0, 6]))


""" Optimised """

def leaders(nums):
    maxi, result = float('-inf'), []
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > maxi:
            maxi = nums[i]
            result.append(maxi)
    return result