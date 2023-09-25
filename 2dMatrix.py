def matrix(arr,key,m,n):
    i = 0
    j = n - 1

    while i >= 0 and i < m and j >= 0 and j < n:
        if arr[i][j] == key:
            return arr[i][j]
        elif arr[i][j] > key:
            j = j -1
        elif arr[i][j] < key:
            i = i + 1
    return -1
arr = [[10,20,30,40],
       [15,25,30,35],
       [28,29,31,32],
       [45,46,47,48]]
key = 29
m = len(arr)
n = len(arr[0])
print("Required position= ",matrix(arr,key,m,n))