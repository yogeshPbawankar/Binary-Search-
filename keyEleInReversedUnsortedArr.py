def peak(arr, key):
    st = 0
    end = len(arr) - 1
    while st <= end:
        mid = st + (end - st) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            if arr[mid] == key:
                return mid
            val1 = ascending(0, mid - 1, key, arr)
            val2 = descending(mid, len(arr) - 1, key, arr)

            if val1 == -1 and val2 == -1:
                return "Key is not present"
            else:
                return max(val1, val2)

        elif arr[mid - 1] > arr[mid]:
            end = mid - 1
        else:
            st = mid + 1
    return "Key is not present"

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

arr = [2, 3, 6, 7, 12, 5, 3, 1]
key = 4
print("Required key:", peak(arr, key))
