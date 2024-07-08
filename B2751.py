import sys

def merge_sort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        leftArr = merge_sort2(arr[:mid])
        rightArr = merge_sort2(arr[mid:])
        return merge(leftArr, rightArr)
    
def merge(leftArr, rightArr):
    leftIndex = rightIndex = 0
    result = []
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            result.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            result.append(rightArr[rightIndex])
            rightIndex += 1
    result.extend(leftArr[leftIndex:])
    result.extend(rightArr[rightIndex:])
    return result

num = int(sys.stdin.readline().rstrip())
numlist = [int(sys.stdin.readline().rstrip()) for i in range(num)]

sorted_list = merge_sort2(numlist)

for item in sorted_list:
    sys.stdout.write(str(item) + '\n')