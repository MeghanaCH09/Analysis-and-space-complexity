def binaryval(arr, low, high, target):
    return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binaryval(arr,mid+1,high,target)
    else:
        return binaryval(arr,low,mid-1,target)