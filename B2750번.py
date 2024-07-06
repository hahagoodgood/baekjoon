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

num = int(input())
numlist = [int(input()) for i in range(num)]

sorted_list = quick_sort(numlist)

for item in sorted_list:
    print(item)
