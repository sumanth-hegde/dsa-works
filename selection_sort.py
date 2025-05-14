arr = [13, 46, 24, 52, 20, 9]

n = len(arr)

for i in range(n-1):
    for j in range(i + 1, n):
        mini = i
        if arr[j] < arr[mini]:
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i]

print(arr)
