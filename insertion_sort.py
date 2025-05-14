class InsertionSort:
    def solution(self, arr):
        arr_len = len(arr)
        for i in range(arr_len):
            j = i
            while j>0 and arr[j - 1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j-=1
        return arr

sol = InsertionSort()
print(sol.solution([13, 46, 24, 52, 20, 9]))
