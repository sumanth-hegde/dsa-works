class BubbleSort:
    def solution(self, arr):
        arr_len = len(arr)
        for i in range(arr_len-1):
            swap = False
            for j in range(0, arr_len - 1 - i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = True
            if not swap:
                break
        return arr

bubble_sort = BubbleSort()
print(bubble_sort.solution([13, 46, 24, 52, 20, 9]))