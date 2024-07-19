import sys
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        littleArr, equalArr, bigArr = [], [], []
        pivot = arr[len(arr)//2]
        for item in arr:
            if item < pivot:
                littleArr.append(item)
            elif item > pivot:
                bigArr.append(item)
            else:
                equalArr.append(item)
        return quick_sort(littleArr) + equalArr + quick_sort(bigArr)
    
def binary_search(Arr, Item):
    left, right = 0, len(Arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if Arr[mid] == Item:
            return 1
        elif Arr[mid] < Item:
            left = mid + 1
        else :
            right = mid - 1
    return 0

    
N = int(sys.stdin.readline().rstrip())
NArr = list(map(int, sys.stdin.readline().rstrip().split()))
NArr = NArr[:N]
NArr = quick_sort(NArr)
M = int(sys.stdin.readline().rstrip())
MArr = list(map(int, sys.stdin.readline().rstrip().split()))
for item in MArr:
    isFind = binary_search(Arr=NArr, Item=item)
    sys.stdout.write(str(isFind) + '\n')


