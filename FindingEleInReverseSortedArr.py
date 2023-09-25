def smallEleInReversedSortedArr(arr, key):
    st = 0
    end = len(arr) - 1
    while st <= end:
        mid = st + (end - st) // 2
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
            if arr[mid] == key:
                return mid
            else:
                val1 = ascending(0, mid -1, key, arr)
                val2 = descending(mid, len(arr) - 1, key, arr)
                return max(val1,val2)

        elif arr[mid] > arr[end]:
            st = mid + 1
        else:
            end = mid - 1
    return -1  # If not found

def descending(st, end, key, arr):
    while st <= end:
        mid = st + (end - st) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            st = mid + 1
        else:
            end = mid - 1
    return -1

def ascending(st, end, key, arr):
    while st <= end:
        mid = st + (end - st) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            st = mid + 1
        else:
            end = mid - 1
    return -1

arr = [11, 13, 4, 6, 8]
key = 6
index = smallEleInReversedSortedArr(arr, key)
if index != -1:
    print("Index of the key:", index)
else:
    print("Key not found in the array.")
