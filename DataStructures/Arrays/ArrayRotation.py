
def leftRotate(arr, d, n):
    if n == 1 :
        print(arr[0])
    else:
        for i in range(d):
            leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr, n):
    for i in range(n):
        print(arr[i])

arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, len(arr))
printArray(arr, len(arr))