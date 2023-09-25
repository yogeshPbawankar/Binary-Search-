def binarySearch(arr,key):
    st = 0
    end = len(arr)-1
    first,last= 0,0
    while st <= end:
        mid = (st + (end -st)//2)
        if arr[mid] == key:
            last = mid
            st = mid + 1 # increasing mid it give 'last_Ocur'
        elif arr[mid] > key:
            end = mid -1
        else:
            st = mid +1
    st = 0
    end = len(arr) -1
    while st <= end:
        mid = (st + (end -st)//2)
        if arr[mid] == key:
            first = mid
            end = mid -1
        elif arr[mid] > key:
            end = mid -1 # lowering mid it give 'first_Ocur'
        else:
            st = mid + 1

    return first,last
arr = [1,3,4,5,5,5,5,6,7,8,9]
val = binarySearch(arr, 5)
print("First_Ocur= ",val)
