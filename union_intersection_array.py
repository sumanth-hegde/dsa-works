def union_intersection_array(arr1, arr2):
    union = set(arr1+arr2)
    intersection = [arr1[i] for i in range(len(arr1)) if arr1[i] in arr1 and arr1[i] in arr2]
    return list(union), intersection


print(union_intersection_array([1,2,4,5,6,7,8], [1,2,3,4]))