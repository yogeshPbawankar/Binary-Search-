def binaySearch(st,end,key,arr):
    if st <= end:
        mid = (st+(end -st)//2)

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binaySearch(st,mid-1,key,arr)
        else:
            return binaySearch(mid+1,end,key,arr)
    return -1

def findPosition(arr,key):
    st , h , val = 0,1,arr[0]
    while key > val and h < len(arr):
        st = h
        h = 2*h
        val = arr[min(h,len(arr)-1)]
    return binaySearch(st,min(h,len(arr)-1),key,arr)
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
key = 140
val = findPosition(arr,key)
if val != -1:
    print("Required position: ",val)
else:
    print("key is not found")