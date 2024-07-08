import sys

def bubble_sort(numlist):
    for i in range(len(numlist)):
        for j in range(len(numlist)-i-1):
            if numlist[j] > numlist[j+1] :
                temp = numlist[j]
                numlist[j] = numlist[j+1]
                numlist[j+1] = temp 
    return numlist
    
def insert_sort(numList):
    for i in range(1, len(numList)):
        key = numList[i]
        j = i-1
        while j>=0 and key < numList[j]:
            numList[j + 1] = numList[j]
            j -= 1
    # 앞서 j-=1을 하였기에 numList에서는 numList[j+1]을 하여야 한다.
        numList[j+1] = key 
    return numList

def select_sort(numList):
    for i in range(len(numList)-1):
        j, min = i, i
        for j in range(i+1, len(numList)):
            if numList[min] > numList[j]:
                min = j
        numList[i], numList[min] = numList[min], numList[i]
    return numList                
 
def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    else : 
        pivot = arr[len(arr)//2]
        littleArr, equalArr, bigArr, = [], [], []
        for item in arr :
            if item < pivot:
                littleArr.append(item)
            elif item > pivot:
                bigArr.append(item)
            else:
                equalArr.append(item)
    return quick_sort(littleArr) + equalArr + quick_sort(bigArr)

def merge_sort(arr) :
    if len(arr) <= 1:
        return arr
    else :
        leftArr, rightArr = arr[:len(arr)//2], arr[len(arr)//2:]
        leftReturn, rightReturn  = merge_sort(leftArr), merge_sort(rightArr)
        leftIndex, rightIndex = 0, 0
        resultArr = [] # 반환값을 넣을 list
        while leftIndex < len(leftReturn) and rightIndex < len(rightReturn):
            if leftReturn[leftIndex] < rightReturn[rightIndex] :
                resultArr.append(leftReturn[leftIndex])
                leftIndex += 1
            elif leftReturn[leftIndex] > rightReturn[rightIndex] :
                resultArr.append(rightReturn[rightIndex])
                rightIndex += 1
            else :
                resultArr.append(leftReturn[leftIndex])
                resultArr.append(rightReturn[rightIndex])
                leftIndex += 1
                rightIndex += 1
        resultArr.extend(leftReturn[leftIndex:])
        resultArr.extend(rightReturn[rightIndex:])
        return resultArr

def merge_sort2(arr):
    if len(arr) <= 1:
        return arr
    else :
        mid = len(arr)//2
        leftArr = merge_sort2(arr[:mid])
        rightArr = merge_sort2(arr[mid:])
        return merge(leftArr, rightArr)

def merge(leftArr, rightArr):
    leftIndex = rightIndex = 0
    result = []
    while leftIndex < len(leftArr) and rightIndex < len(rightArr) :
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

# 적용하고 싶은 함수를 적용하여 해결하시오! 
sorted_list = insert_sort(numlist) 

for item in sorted_list:
    sys.stdout.write(str(item) + '\n')
