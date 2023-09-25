def smallEleInReversedSortedArr(arr):
    st = 0
    end = len(arr) - 1
    while st <= end:
        mid = st + (end - st) // 2
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
            return mid
        elif arr[mid] > arr[end]:
            st = mid + 1
        else:
            end = mid - 1
    return -1  # If not found

arr = [11,13, 4, 6, 8]
index = smallEleInReversedSortedArr(arr)
if index != -1:
    print("Index of smallest element:", index)
else:
    print("Smallest element not found in the array.")
