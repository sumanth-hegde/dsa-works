class RecursiveBubbleSort:
    def solution(self, arr, n):
        if n == 1:
            return arr
        swap = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
        if not swap:
            return arr
        return self.solution(arr, n-1)

sort = RecursiveBubbleSort()
arr = [3,2,1,4,5]
print(sort.solution(arr, len(arr)))